from django.contrib import admin
from .models import Account
from import_export.admin import ImportExportModelAdmin


class AccountAdmin(ImportExportModelAdmin):
    model = Account
    list_display = ['uuid', 'title', 'name', 'gender', 'branch',
                    'designation', 'phone', 'created_on', 'updated_on']
    search_fields = ('uuid', 'name')
    list_filter = ('title', 'designation', 'branch')


admin.site.register(Account, AccountAdmin)
