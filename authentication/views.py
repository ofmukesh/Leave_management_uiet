from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from leave_management_uiet import configs
from .forms import ForgotPassForm
from services.email import compose_email
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.auth.hashers import make_password
from accounts.models import Account
from account_status.models import Status
from services.email import compose_email
from django.template.loader import render_to_string
from leave_types.models import LeaveType


def userlogin(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    context = {}
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login if account is acitvated
            if Account.objects.filter(user=user.id).exists():
                ac = Account.objects.get(user=user.id)
                if ac.activated:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    url = generate_reset_pass_url(user)
                    message = render_to_string(
                        'mails/reset_pass_request.html', context={'url': url})
                    compose_email(to=[user.username],
                                  subject="Password reset request!", body=message)

                    return render(request, 'pages/activate_account.html', context)
            else:
                login(request, user)
                return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Username or Password did not match")
    context['form'] = form
    return render(request, 'forms/login.html', context)


def userlogout(request):
    if request.method == 'GET':
        logout(request)
    return HttpResponseRedirect('/auth/login/')


def generate_reset_pass_url(username):
    user = User.objects.get(username=username)

    if user:
        url = configs.DOMAIN + "/accounts/reset/" + \
            urlsafe_base64_encode(force_bytes(user.pk)) + \
            "/" + default_token_generator.make_token(user)+"/"
    return url


def forgot_pass(request):
    context = {}
    form = ForgotPassForm()
    if request.method == 'POST':
        form = ForgotPassForm(request.POST)
        if form.is_valid():
            url = generate_reset_pass_url(username=form.cleaned_data['email'])
            message = render_to_string(
                'mails/reset_pass_request.html', context={'url': url})
            compose_email(to=[form.cleaned_data['email']],
                          subject="Password reset request!", body=message)
            messages.success(
                request, "Password reset mail sent to your registered email address.")
            return HttpResponseRedirect("/auth/login/")
    context['form'] = form
    return render(request, 'forms/forgot_pass.html', context)


# create user account + send mail success
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
    message = render_to_string(
        'mails/register_success.html', context=form)
    compose_email(to=[form['username']],
                  subject="Registered succesfully to UIET Leave management portal", body=message)

    return form['uuid']
