from . import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from home.views import home

admin.site.site_header = "University Institute of Engg. & Technology"
admin.site.site_title = "Uiet"

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('auth/', include('auth.urls')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
