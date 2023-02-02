from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Application
from django.http import HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest
from django.contrib import messages


@login_required(login_url='/auth/login/')
def applications(request):
    if request.user.is_staff:
        context = {'applications': Application.objects.all().filter(
            status="Pending")}
        return render(request, 'pages/applications.html', context)
    return HttpResponseNotFound()


@login_required(login_url='/auth/login/')
def view_application(request, pk):
    context = {'application': Application.objects.get(trace_id=pk)}
    context['eligible_cancel'] = True
    return render(request, 'pages/view_application.html', context)


@login_required(login_url='/auth/login/')
def update_application(request, pk, status):

    if status == 'cancel':
        if not request.user.is_staff and not request.user.is_superuser:
            messages.info(request, 'Done')
            return HttpResponse("Done")
        else:
            messages.warning(request, 'Permission denied')
            return HttpResponseForbidden('Permission denied')

    elif status == 'approve' or status == 'reject':
        if request.user.is_staff:
            messages.info(request, 'Done')
            return HttpResponse("Done")
        else:
            messages.warning('Permission denied')
            return HttpResponseForbidden('Permission denied')

    return HttpResponseBadRequest("something went wrong 😔")
