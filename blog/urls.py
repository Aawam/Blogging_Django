from django.urls import path

from .views import *

urlpatterns = [
    path('', article_list, name='article_list'),
    path('<str:pk>/', article_detail, name='article_detail'),
    path('create/new/', article_create, name='article_create'),
    path('<str:pk>/edit/', article_update, name='article_update'),
    path('<str:pk>/delete/', article_delete, name='article_delete'),
    
    path('categories', categories_list, name='categories_list'),

    path('tags', tags_list, name='tags_list')
]
