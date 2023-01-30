from django.db import models
from accounts.models import Account
from leave_types.models import LeaveType


class Status(models.Model):
    uuid = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(LeaveType, on_delete=models.SET_NULL, null=True)
    total = models.IntegerField(default=0)
    availed = models.FloatField(default=0)
    balance = models.FloatField(default=0)
    applied = models.IntegerField(default=0)
    applied_days = models.FloatField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
