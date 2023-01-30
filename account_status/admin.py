from django.contrib import admin
from .models import Status

# Register your models here.


class StatusAdmin(admin.ModelAdmin):
    model = Status
    list_display = ['name', 'type', 'total', 'availed', 'balance',
                    'applied', 'applied_days', 'created_on', 'updated_on']

    def name(self, obj):
        return obj.uuid.title+' '+obj.uuid.name+' ('+obj.uuid.uuid+')'


admin.site.register(Status, StatusAdmin)