from django.urls import path
from superadmin import views


urlpatterns = [
    path('register/', views.register_user, name='register_user'),
]
