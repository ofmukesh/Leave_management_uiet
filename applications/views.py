from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Application
from django.http import HttpResponseNotFound
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
    if request.user.is_staff:
        context = {'application': Application.objects.get(trace_id=pk)}
        return render(request, 'pages/view_application.html', context)
    return HttpResponseNotFound()


@login_required(login_url='/auth/login/')
def update_application(request, pk, status):
    if request.user.is_staff:
        print(status)
        context = {'application': Application.objects.get(trace_id=pk)}
        messages.info(request, 'done')
        return HttpResponse("done", status=200)
    return HttpResponseNotFound()
