from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

from users.models import CustomUser

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title

class Blog_Article(models.Model):
    title = models.CharField(
        max_length=100, 
        primary_key=True,     
    )
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)
    date_created = models.DateField(auto_now_add=True,editable=True)
    text=CKEditor5Field('Text', config_name='extends')
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    class Meta:
        ordering = ['title']
    