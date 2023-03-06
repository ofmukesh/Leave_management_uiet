from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegisterForm
from leave_types.models import LeaveType
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from authentication.views import register


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
