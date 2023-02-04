from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegisterForm
from leave_types.models import LeaveType
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from accounts.models import Account
from account_status.models import Status
from services.email import compose_email
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from authentication.views import generate_reset_pass_url


@login_required(login_url="/admin/login/?next=/superadmin/")
def register_user(request):
    context = {}
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = register(form.cleaned_data, request.POST)
            messages.success(
                request, f'User account registered successfully uuid( {user["uuid"]} )')
            return HttpResponseRedirect('/superadmin/register/')
    context['form'] = form
    context['status_form'] = LeaveType.objects.all()
    return render(request, 'forms/register_form.html', context)


def register(form, leave_form):
    # creating user
    user = User(username=form['username'], password=make_password(
        password=form['username']))
    user.save()

    # # creating account for user
    ac = Account(title=form['title'], name=form['name'], gender=form['gender'], branch=form['branch'],
                 phone=form['phone'], designation=form['designation'], user=user,)
    ac.save()

    # creating leave status for account
    leaves = LeaveType.objects.all().values('leave_name', 'id')
    for leave in leaves:
        leave_type = LeaveType.objects.get(leave_name=leave['leave_name'])
        leave_status = Status(uuid=ac, type=leave_type, total=int(
            leave_form[leave['leave_name']][0]), balance=int(
            leave_form[leave['leave_name']][0]))
        leave_status.save()

    # sending mail to registered user
    form['uuid'] = Account.objects.values('uuid').get(
        user=User.objects.get(username=form['username']))  # uuid of created user
    form['reset_pass'] = generate_reset_pass_url(form['username'])
    message = render_to_string(
        'mails/register_success.html', context=form)
    compose_email(to=[form['username']],
                  subject="Registered succesfully to UIET Leave management portal", body=message)

    return form['uuid']
