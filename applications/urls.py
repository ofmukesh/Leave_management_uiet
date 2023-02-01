from django.urls import path
from . import views

urlpatterns = [
    path('', views.applications, name='applications'),
    path('<str:pk>/', views.view_application, name='view_application'),
    path('<str:pk>/<slug:status>/',
         views.update_application, name='update_application'),
]
