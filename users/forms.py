from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("name", "email", "password")
        widgets = {
            "name" : forms.TextInput(),
            "email" : forms.EmailInput(),
            "password" : forms.PasswordInput()
        }


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("name", "email", "password")
        widgets = {
            "name" : forms.TextInput(),
            "email" : forms.EmailInput(),
            "password" : forms.PasswordInput()
        }
class LoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'password']
        widgets = {
            'name' : forms.TextInput,
            'password': forms.PasswordInput()
        }
