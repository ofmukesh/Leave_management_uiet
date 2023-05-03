from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('<str:uuid>/', views.account_info, name='account info'),
]
