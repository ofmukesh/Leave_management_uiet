from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from accounts.models import Account


@login_required(login_url='/auth/login/')
def get_account(request):
    if Account.objects.filter(user=request.user).exists():
        uuid = Account.objects.get(user=request.user)
        return Account.objects.get(uuid=uuid)
    return None


@login_required(login_url='/auth/login/')
def profile(request):
    context = {'account': get_account(request)}
    return render(request, 'pages/profile.html', context)
