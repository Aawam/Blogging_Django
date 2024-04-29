from django.urls import path

from .views import *


urlpatterns = [
    path('', article_list, name='article_list'),
    path('<str:pk>/', article_detail, name='article_detail'),
    path('create/new/', article_create, name='article_create'),
    path('<str:pk>/edit/', article_update, name='article_update'),
    path('<str:pk>/delete/', article_delete, name='article_delete'),
    
    #------------------
    path('categories', categories_list, name='categories_list'),    
    path('categories/new/', categories_create, name='categories_create'),
    #path('categories/<str:pk>/edit/', categories_update, name='categories_update'),
    path('categories/<str:pk>/delete/', categories_delete, name='categories_delete'),

    #------------------
    path('tags', tags_list, name='tags_list'),    
    path('tags/new/', tags_create, name='tags_create'),
    #path('tags/<str:pk>/edit/', tags_update, name='tags_update'),
    path('tags/<str:pk>/delete/', tags_delete, name='tags_delete'),
]
