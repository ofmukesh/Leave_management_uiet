from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/auth/login/')
def home(request):
    if request.user.is_superuser:
        return render(request, "super_admin.html")
    elif request.user.is_staff:
        return render(request, "/pages/director.html")
    else:
        return render(request, "/pages/user.html")
