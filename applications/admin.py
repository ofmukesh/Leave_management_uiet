from django.contrib import admin
from .models import Application


class ApplicationAdmin(admin.ModelAdmin):
    model = Application
    list_display = ['trace_id', 'name', 'type', 'reason', 'date_from', 'date_to',
                    'status', 'created_on', 'updated_on']

    def name(self, obj):
        return obj.uuid.title+' '+obj.uuid.name


admin.site.register(Application, ApplicationAdmin)
