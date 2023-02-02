from django.urls import path
from . import views

urlpatterns = [
    path('', views.applications, name='applications'),
    path('staff_history/', views.applications_history,
         name='applications_history'),
    path('history/', views.history, name='history'),
    path('history/<int:leave_type>/', views.leave_history, name='leave_history'),
    path('<str:pk>/', views.view_application, name='view_application'),
    path('<str:pk>/<slug:status>/',
         views.update_application, name='update_application'),
]
