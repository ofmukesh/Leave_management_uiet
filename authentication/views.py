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


def userlogin(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    context = {}
    form = AuthenticationForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')

    context['form'] = form
    return render(request, 'pages/login.html', context)


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
            return HttpResponseRedirect("/auth/forgot_password/")
    context['form'] = form
    return render(request, 'forms/forgot_pass.html', context)
