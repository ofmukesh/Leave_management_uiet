from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from leave_management_uiet import configs


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
