from django.db import models

# Create your models here.
class Authors(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=225)