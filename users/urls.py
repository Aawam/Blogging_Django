from django.contrib import admin
from django.urls import path, include

from .views import dashboard_view, register_view, \
    login_view, logout_view, \
        delete_user, edit_user, \
        user_view, pass_change

app_name = 'users'

urlpatterns = [

    path('<str:pk>/dashboard/', dashboard_view, name='dashboard'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('<str:pk>/', user_view, name='user_view'),
    path('<str:pk>/delete/', delete_user, name='delete_user'),
    path('<str:pk>/edit/', edit_user, name='edit_user'),
    path('<str:pk>/password/', pass_change, name='pass_change')
]

