from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ]

    username = models.CharField(primary_key=True)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    birth_place = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='user_photos/', blank=True)
    about = models.TextField(blank=True)

    def __str__(self):
        return self.username