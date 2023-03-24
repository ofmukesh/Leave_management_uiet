from . import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from home.views import home
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from authentication.views import CustomPasswordResetConfirmView

admin.site.site_header = "University Institute of Engg. & Technology"
admin.site.site_title = "Uiet"

urlpatterns = [
    path('', home, name='home'),
    path('applications/', include('applications.urls')),
    path('superadmin/', include('superadmin.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('account/', include('accounts.urls')),
    path('accounts/reset/<uidb64>/<token>/',
         CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', RedirectView.as_view(url="/auth/login/"),
         name='password_reset_complete'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
