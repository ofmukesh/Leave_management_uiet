from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Application
from django.http import HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest
from django.contrib import messages
from accounts.views import get_account
from .forms import LeaveApplyForm
from leave_management_uiet import configs
from django.template.loader import render_to_string
from services.email import compose_email
from account_status.models import Status
from datetime import datetime


@login_required(login_url='/auth/login/')
def applications(request):
    if request.user.is_staff:
        context = {'applications': Application.objects.all().filter(
            status="Pending")}
        return render(request, 'pages/applications.html', context)
    return HttpResponseNotFound()


@login_required(login_url='/auth/login/')
def view_application(request, pk):
    application = Application.objects.get(trace_id=pk)
    context = {'application': application, 'eligible_cancel': True}
    curr_date = datetime.now().date()
    curr_time = datetime.now().time()
    if (application.status != 'Pending') or (curr_date > application.date_from) or (curr_date == application.date_from and curr_time.hour > 9):
        context['eligible_cancel'] = False
    return render(request, 'pages/view_application.html', context)


@login_required(login_url='/auth/login/')
def update_application(request, pk, status):
    application = Application.objects.get(trace_id=pk)
    leave_status = Status.objects.get(
        uuid=application.uuid.uuid, type=application.type.id)

    if not application or not leave_status:
        messages.error(request, 'application or leave data not found')
        return HttpResponse("application or leave data not found")

    if status == 'cancel':
        if not request.user.is_staff and not request.user.is_superuser and (request.user.username == application.uuid.user.username):
            curr_date = datetime.now().date()
            curr_time = datetime.now().time()
            if (application.status != 'Pending') or (curr_date > application.date_from) or (curr_date == application.date_from and curr_time.hour > 9):
                messages.error(request, 'not eligible to cancel for now')
                return HttpResponse("not eligible to cancel for now")

            # if user eligible to cancel then process>>
            leave_status.applied_days -= application.days
            leave_status.applied -= 1
            application.status = 'Cancelled'
            leave_status.save()
            application.save()
            context = {'application': application}
            template = render_to_string(
                'mails/response_application.html', context)
            compose_email(
                to=[request.user.username], subject=f"Application cancelled!", body=template)
            return HttpResponse("Process done")
        else:
            messages.warning(request, 'Permission denied')
            return HttpResponseForbidden('Permission denied')

    elif status == 'approve' or status == 'reject':
        if request.user.is_staff:
            messages.info(request, 'Done')
            if status == 'approve':
                leave_status.applied_days -= application.days
                leave_status.applied -= 1
                leave_status.balance -= application.days
                leave_status.availed += application.days
                application.status = 'Approved'
            else:
                leave_status.applied_days -= application.days
                leave_status.applied -= 1
                application.status = 'Rejected'
            leave_status.save()
            application.save()
            context = {'application': application}
            template = render_to_string(
                'mails/response_application.html', context)
            compose_email(
                to=[application.uuid.user.username], subject=f"Application {application.status}!", body=template)
            messages.success(request, f"Application {application.status}")
            return HttpResponse("Done")
        else:
            messages.warning(request, 'Permission denied')
            return HttpResponseForbidden('Permission denied')

    return HttpResponseBadRequest("something went wrong 😔")


@login_required(login_url='/auth/login/')
def applications_history(request):
    if request.user.is_staff:
        context = {'applications': Application.objects.all().exclude(
            status='Pending')}
        return render(request, 'pages/staff_history.html', context)
    return HttpResponseNotFound()


@login_required(login_url='/auth/login/')
def history(request):
    uuid = get_account(request).uuid
    context = {'applications': Application.objects.all().filter(
        uuid=uuid).exclude(status='Pending')}
    return render(request, 'pages/history.html', context)


@login_required(login_url='/auth/login/')
def leave_history(request, leave_type):
    uuid = get_account(request).uuid
    context = {'applied': Application.objects.all().filter(
        uuid=uuid, status='Pending', type=leave_type)}
    return render(request, 'pages/leave_history.html', context)


@login_required(login_url='/auth/login/')
def apply(request):
    context = {}
    form = LeaveApplyForm()
    if request.method == 'POST':
        form = LeaveApplyForm(request.POST)
        if form.is_valid():
            # 1 user data from database
            leave_type = form.cleaned_data['type']
            account = get_account(request)
            leave_status = Status.objects.get(
                uuid=account.uuid, type=leave_type.id)
            balance = leave_status.balance-leave_status.applied_days

            # 1.1 checking user data is exist or not
            if not account:
                return HttpResponseNotFound('Account not found')
            if not leave_status:
                return HttpResponseNotFound('Leave data not found')

            # 2 form data
            date_from = form.cleaned_data['date_from']
            date_to = form.cleaned_data['date_to']
            days = (date_to-date_from).days+1
            time_period = form.cleaned_data['time_period']

            # 2.1 if time_period is not full day + only for Non-teaching
            if time_period != 'Day' and account.designation == 'Non-Teaching':
                days = 0.5
                date_to = date_from
            elif account.designation != 'Non-Teaching':
                time_period = 'Day'

            # 2.2 process application if user is eligible
            if days <= 0:
                messages.error(request, 'Invalid date!')
            elif balance <= 0 or balance < days:
                messages.warning(request, 'Insufficient balance!')
            else:
                # 2.3 application data from form
                reason = form.cleaned_data['reason']
                station_leave = form.cleaned_data['station_leave']

                # 2.4 creating application
                new_application = Application(type=leave_type, time_period=time_period, reason=reason,
                                              days=days, date_from=date_from, date_to=date_to, station_leave=station_leave, uuid=account)

                # if application created
                if new_application:
                    # 2.5 updating leave status
                    leave_status.applied += 1
                    leave_status.applied_days += days

                    # 2.6 mail template & context setup
                    context = {'application': new_application,
                               'link': configs.DOMAIN+f"/applications/{new_application.trace_id}"}
                    teacher_template = render_to_string(
                        template_name='mails/teacher_application.html', context=context)
                    director_template = render_to_string(
                        template_name='mails/director_application.html', context=context)

                    # 2.7 sending mail to user and staff
                    teacher_mail = compose_email(
                        to=[request.user.username], subject=f"Application submitted!", body=teacher_template)
                    if teacher_mail:
                        director_mail = compose_email(to=configs.APPLICATON_STAFF_MAILS, subject="Application for leave",
                                                      body=director_template)
                        if director_mail:
                            new_application.save()
                            leave_status.save()
                            messages.success(request, 'Application submitted')
                            return HttpResponseRedirect('/applications/apply/')
                        else:
                            messages.error(
                                request, 'mail not send to Director')
                    else:
                        messages.error(request, 'mail not send to user')
                else:
                    messages.error(request, 'Application not created...')

    context['account'] = get_account(request)
    context['form'] = form
    return render(request, 'forms/leave_form.html', context)
