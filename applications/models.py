from django.db import models
from accounts.models import Account
from leave_types.models import LeaveType
from utils.choices import FieldChoices
import uuid


def TraceId():
    return uuid.uuid4().hex[0:15]


class Application(models.Model):
    trace_id = models.CharField(
        default=TraceId, editable=False, primary_key=True, max_length=15)
    type = models.ForeignKey(
        LeaveType, on_delete=models.PROTECT, null=False, blank=False)
    reason = models.TextField()
    days = models.FloatField()
    time_period = models.CharField(
        choices=FieldChoices.timePeriodChoices(), max_length=30, default='Day')
    date_from = models.DateField()
    date_to = models.DateField()
    station_leave = models.BooleanField(default=False)
    status = models.CharField(
        choices=FieldChoices.leaveStatusChoices(), default='Pending', max_length=30)
    uuid = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
