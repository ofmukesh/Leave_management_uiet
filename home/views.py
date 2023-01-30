from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from accounts import views


@login_required(login_url='/auth/login/')
def home(request):
    if request.user.is_superuser:
        return superadmin_home(request)
    elif request.user.is_staff:
        return director_home(request)
    elif request.user.is_authenticated:
        return teacher_home(request)
    return HttpResponseBadRequest("User not found")


def superadmin_home(request):
    if request.user.is_superuser:
        return render(request, "super_admin.html")


def director_home(request):
    return render(request, "pages/director.html")


def teacher_home(request):
    account = views.get_account(request)
    return render(request, "pages/user.html")
