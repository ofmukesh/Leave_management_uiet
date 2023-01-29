from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect


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
    return render(request, 'login.html', context)


def userlogout(request):
    if request.method == 'GET':
        logout(request)
    return HttpResponseRedirect('/auth/login/')
