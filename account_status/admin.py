from django.contrib import admin
from .models import Status
from import_export.admin import ImportExportModelAdmin

# Register your models here.


class StatusAdmin(ImportExportModelAdmin):
    model = Status
    list_display = ['name', 'type', 'total', 'availed', 'balance',
                    'applied', 'applied_days', 'created_on', 'updated_on']
    search_fields = ('uuid__name', 'uuid__uuid')
    list_filter = ('type',)

    def name(self, obj):
        if obj.uuid:
            return obj.uuid.title+' '+obj.uuid.name+' ('+obj.uuid.uuid+')'
        return None


admin.site.register(Status, StatusAdmin)
