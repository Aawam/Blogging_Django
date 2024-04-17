from django import forms
from.models import Blog_Article

class Blog_Form(forms.ModelForm):
    
    class Meta:
        model = Blog_Article

        fields = [
            'Title',
            'Author',
            'Date Created',
        ]