from . import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from home.views import home

admin.site.site_header = "University Institute of Engg. & Technology"
admin.site.site_title = "Uiet"

urlpatterns = [
    path('', home, name='home'),
    path('applications/', include('applications.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('account/', include('accounts.urls')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
