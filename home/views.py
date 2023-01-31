from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from accounts import views as account_view
from account_status import views as status_view
from account_status.serializers import StatusSerializer


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
    account = account_view.get_account(request)
    if account:
        account_status = status_view.get_account_status(account)
        account_status_data = StatusSerializer(account_status, many=True).data
        context = {'leaves_status': account_status_data}
        return render(request, "pages/user.html", context)
    return HttpResponseBadRequest("Account not found")
