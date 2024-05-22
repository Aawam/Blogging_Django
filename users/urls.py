from django.contrib import admin
from django.urls import path, include

from .views import dashboard_view, profile_user, delete_user, edit_user

app_name = 'users'

urlpatterns = [

    path('<str:pk>/dashboard/', dashboard_view, name='dashboard'),
    path('<str:pk>/profile', profile_user, name='profile_user'),
    path('<str:pk>/delete/', delete_user, name='delete_user'),
    path('<str:pk>/edit/', edit_user, name='edit_user'),
    
]

