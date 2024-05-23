from django import forms
from django.contrib.auth.forms import UserChangeForm
from allauth.account.forms import SignupForm, LoginForm

from .models import CustomUser

class CustomUserCreationForm(SignupForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    full_name = forms.CharField(max_length=100, label='Full Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    gender = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    birth_place = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    photo = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    about = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    def save(self, request):
        user = super(CustomUserCreationForm, self).save(request)
        user.full_name = self.cleaned_data['full_name']
        user.gender = self.cleaned_data['gender']
        user.phone_number = self.cleaned_data['phone_number']
        user.birth_place = self.cleaned_data['birth_place']
        user.birth_date = self.cleaned_data['birth_date']
        user.photo = self.cleaned_data['photo']
        user.about = self.cleaned_data['about']
        user.save()
        return user

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'full_name', 'gender', 'phone_number', 'birth_place', 'birth_date', 'photo', 'about']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_place': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'about': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CustomUserLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control'})

"""
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'full_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

#from django.contrib.auth.models import User
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'username', 
            'email', 
            'full_name', 
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
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

class CustomUserLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={'class': 'custom-class'})

        """