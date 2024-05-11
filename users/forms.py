from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

#from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = [
            'username', 
            'email', 
            'full_name', 
            'gender',
            'phone_number',
            'birth_place',
            'birth_date',
            'photo',
            'about',
        ]

        widgets = {
            'username' : forms.TextInput,
            'email' : forms.EmailInput,
            'full_name' : forms.TextInput,
            'phone_number' : forms.NumberInput,
            'gender' : forms.Select,
            'birth_place' : forms.TextInput,
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'photo' : forms.FileInput,
            'about' : forms.Textarea,
        }

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = [
            'full_name', 
            'gender',
            'phone_number',
            'birth_place',
            'birth_date',
            'photo',
            'about',
        ]

        widgets = {
            'full_name' : forms.TextInput,
            'phone_number' : forms.NumberInput,
            'gender' : forms.Select,
            'birth_place' : forms.TextInput,
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'photo' : forms.FileInput,
            'about' : forms.Textarea,
        }