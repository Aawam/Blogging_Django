# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ['username', 'email', 'full_name', 'gender', 'phone_number', 'birth_place', 'birth_date', 'is_staff']

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('full_name', 'gender', 'phone_number', 'birth_place', 'birth_date', 'photo', 'about')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('username', 'email', 'full_name', 'gender', 'phone_number', 'birth_place', 'birth_date', 'photo', 'about', 'password1', 'password2')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)