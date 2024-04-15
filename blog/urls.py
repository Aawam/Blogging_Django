from django.urls import path

from .views import index, display_data, category_list

urlpatterns = [
    path("", index),
    path("display/", display_data),
    path("categories/", category_list)
]
