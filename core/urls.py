"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('article/', include('article.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog.views import article_list, article_detail, article_create, article_update, article_delete

urlpatterns = [
    path('', article_list, name='article_list'),
    path('content/<str:pk>/', article_detail, name='article_detail'),
    path('content/new/', article_create, name='article_create'),
    path('content/<str:pk>/edit/', article_update, name='article_update'),
    path('content/<str:pk>/delete/', article_delete, name='article_delete'),
    #path('create/', create_view, name='create_view'),
    #path('success/', success_view, name='success'),
    

    #path('detailview/<title>/', article_detail ),
    #path('<id>/delete', delete_view),
    
    path('admin/', admin.site.urls),
    #path("users/")
]
