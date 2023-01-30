from django.db import models

# Create your models here.


class LeaveType(models.Model):
    leave_name = models.CharField(max_length=20, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.leave_name