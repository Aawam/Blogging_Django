from django import forms
from.models import Blog_Article, Category, Tag

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
        exclude = [
            'date_created'
        ]

class Category_Form(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["title",]

class Tag_Form(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["title"]
