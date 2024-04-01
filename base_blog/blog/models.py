from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

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

class CustomUserManager(BaseUserManager):
    def create_user(self, acc_name, password=None, **extra_fields):
        if not acc_name:
            raise ValueError(_('The id must be set'))
        acc_id = self.normalize_acc_id(acc_id)
        user = self.model(acc_id=acc_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, acc_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

class CustomUser(AbstractUser):
    acc_id = models.CharField(max_length = 10,primary_key=True, unique=True)

    USERNAME_FIELD = 'acc_id'
    REQUIRED_FIELD = []

    objects = CustomUserManager()

    def __str__(self):
        return self.acc_id