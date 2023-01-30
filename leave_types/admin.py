from django.contrib import admin
from .models import LeaveType

# Register your models here.


class LeaveTypeAdmin(admin.ModelAdmin):
    model = LeaveType
    list_display = ['id','leave_name']

admin.site.register(LeaveType,LeaveTypeAdmin)