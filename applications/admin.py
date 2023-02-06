from django.contrib import admin
from .models import Application


class ApplicationAdmin(admin.ModelAdmin):
    model = Application
    list_display = ['trace_id', 'name', 'type', 'date_from', 'date_to',
                    'status', 'created_on', 'updated_on']
    search_fields = ('trace_id', 'uuid__name', 'uuid__uuid')
    list_filter = ('status', 'type', 'date_from', 'date_to')

    def name(self, obj):
        if obj.uuid:
            return obj.uuid.title+' '+obj.uuid.name
        return None


admin.site.register(Application, ApplicationAdmin)
