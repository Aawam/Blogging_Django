from django import forms
from .models import *

class Category_Form(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["title",]
        widgets = {
            'title' : forms.TextInput,
        }

class Tag_Form(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["title",]
        widgets = {
            'title' : forms.TextInput,
        }

class Blog_Form(forms.ModelForm):
    
    class Meta:
        model = Blog_Article

        fields = [
            'title',
            'categories',
            'tags',
            'author',
            'content',
        ]

        widgets = {
            'tags' : forms.CheckboxSelectMultiple,
            'categories' : forms.Select,
            'content' : forms.Textarea
        }

        exclude = [
            'date_created'
        ]


