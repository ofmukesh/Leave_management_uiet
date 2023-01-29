from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='/auth/login/')
def profile(request):
    context = {}
    return render(request, 'profile.html', context)
