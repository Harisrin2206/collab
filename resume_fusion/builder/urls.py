from django.urls import path
from . import views

urlpatterns = [
    path('members/',views.members),
     path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.master, name='master'),
    path('forms/', views.forms, name='forms'),
    path('design/', views.design, name='design'),
    path('download/', views.download, name='download'),
]