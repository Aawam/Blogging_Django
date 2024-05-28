
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('article/', include('blog.urls'), name='article'),
    path('users/', include('users.urls')),
    path('accounts/', include('allauth.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

