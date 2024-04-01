from django.db import models

class Blog_Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    tag = models.ManyToManyField('Tag')
    author = models.CharField(max_length=50)
    date_created = models.DateField()
    content = models.TextField(null=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
    
class Categories(models.Model):
    title = models.CharField(max_length=200)

class Tag(models.Model):
    title = models.CharField(max_length=100)
