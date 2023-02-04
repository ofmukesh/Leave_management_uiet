from django.db import models
from django.contrib.auth.models import User
from utils.choices import FieldChoices
import uuid


def GenUUID():
    return uuid.uuid4().hex[:10]


class Account(models.Model):
    uuid = models.CharField(max_length=25, default=GenUUID,
                            editable=False, unique=True, primary_key=True)
    title = models.CharField(
        choices=FieldChoices.titleChoices(), max_length=25)
    name = models.CharField(blank=False, null=False, max_length=50)
    gender = models.CharField(
        choices=FieldChoices.genderChoices(), max_length=15)
    branch = models.CharField(
        choices=FieldChoices.branchChoices(), max_length=15)
    phone = models.CharField(max_length=10)
    designation = models.CharField(
        choices=FieldChoices.designationChoices(), max_length=15)
    user = models.OneToOneField(
        User, on_delete=models.SET_NULL, null=True)
    work_status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.uuid