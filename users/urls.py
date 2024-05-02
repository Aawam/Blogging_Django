from django.urls import path

from .views import *


urlpatterns = [
    path('', homepage, name=""),
    path('register/', register, name="register"),
    path('login/', login , name="login"),
    path('dashboard/', dashboard , name="dashboard"),
    path('logout/', logout, name="logout"),
]