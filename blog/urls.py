from django.urls import path
from blog import views

urlpatterns = [
    path('', views.list_view, name='list'),
    path('blog/<int:pk>/', views.detail_view, name='blog_detail'),
    path('blog/new/', views.create_article, name='blog_create'),
    path('blog/<int:pk>/edit/', views.update_article, name='blog_update'),
    path('blog/<int:pk>/delete/', views.article_delete, name='blog_delete'),
]