from django.contrib import admin
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    model = Account
    list_display = ['uuid', 'title', 'name', 'gender', 'branch',
                    'designation', 'phone', 'email', 'work_status', 'created_on', 'updated_on']


admin.site.register(Account, AccountAdmin)
