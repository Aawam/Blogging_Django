from django import forms
from .models import *

from django_ckeditor_5.widgets import CKEditor5Widget

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
            'text',
        ]

        widgets = {
            'tags' : forms.CheckboxSelectMultiple,
            'categories' : forms.Select,
            "text": CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="extends"
              )
        }

        exclude = [
            'date_created'
            'author'
        ]


