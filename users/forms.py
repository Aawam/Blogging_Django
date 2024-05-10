from django import forms
from . import models

from django.contrib.auth.models import User

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name'] 