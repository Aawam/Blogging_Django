from django.contrib import admin
from django.urls import path, include

from .views import dashboard_view, register_view, login_view, logout_view

app_name = 'users'

urlpatterns = [

    path('', dashboard_view, name='index'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout')

]

