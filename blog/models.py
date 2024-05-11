from django.db import models

# Create your models here.

from users.models import CustomUser

class Category(models.Model):
    title = models.CharField(max_length=100,)

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Blog_Article(models.Model):
    title = models.CharField(
        max_length=100, 
        primary_key=True,     
    )
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)
    date_created = models.DateField(auto_now_add=True,editable=True)
    content = models.TextField(null=True)
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    class Meta:
        ordering = ['title']
    