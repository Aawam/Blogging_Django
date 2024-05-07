from django.urls import path

from .views import *

app_name = 'users'

urlpatterns = [

    path('', homepage, name="homepage"),
    path('register/', register, name="register"),
    path('login/', login , name="login"),
    path('dashboard/', dashboard , name="dashboard"),
    path('logout/', logout, name="logout"),
    
]