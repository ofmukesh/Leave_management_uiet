from . import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from home.views import home
from django.contrib.auth import views as auth_views

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
         auth_views.PasswordResetConfirmView.as_view(template_name='forms/reset_pass_form.html'), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='pages/reset_pass_done.html'),
         name='password_reset_complete'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
