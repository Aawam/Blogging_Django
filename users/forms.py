from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django import forms
from django.forms.widgets import PasswordInput, TextInput


# - > Create / Register a User (Model Form)

class CreateUserForm(UserCreationForm):

    class Meta:

        model = get_user_model()
        fields = ['email', 'password1', 'password2']
        widgets = {
            'email' : forms.EmailInput(),
            'password1' : forms.PasswordInput(),
            'password2' : forms.PasswordInput(),
        }

# - > Authentication a User 

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

    