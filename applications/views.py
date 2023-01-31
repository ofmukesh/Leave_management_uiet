from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Application
from django.http import HttpResponseNotFound


@login_required(login_url='/auth/login/')
def applications(request):
    if request.user.is_staff:
        context = {'applications': Application.objects.all().filter(
            status="Pending")}
        return render(request, 'pages/applications.html', context)
    return HttpResponseNotFound()
