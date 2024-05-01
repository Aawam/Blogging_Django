from django.urls import path

from .views import *

urlpatterns = [
    path('login/', user_login, name='user_login'),
    path('signup/', user_signup, name='user_signup'),
    path('logout/', user_logout, name='user_logout')
]



'''urlpatterns = [

    path('register', user_register , name="user_register"),
    path('login', user_login , name="user_login"),
    path('dashboard', user_dashboard , name="user_dashboard")
]'''