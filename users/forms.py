from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User

from django import forms
from django.forms.widgets import PasswordInput, TextInput
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

# - > Create / Register a User (Model Form)

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']

# - > Authentication a User 

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

    