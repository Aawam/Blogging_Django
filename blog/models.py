from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Blog_Article(models.Model):
    title = models.CharField(max_length=100)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    author = models.CharField(max_length=50)
    date_created = models.DateField()
    content = models.TextField(null=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
    