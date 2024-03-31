from django.contrib import admin
from .models import Authors

# Register your models here.

class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email',)

admin.site.register(Authors, AuthorsAdmin)