from django import forms
from.models import Blog_Article

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