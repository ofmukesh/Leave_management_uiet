from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Status


@login_required(login_url='/auth/login/')
def get_account_status(account):
    if Status.objects.filter(uuid=account.uuid).exists():
        return Status.objects.all().filter(uuid=account.uuid)
    return None
