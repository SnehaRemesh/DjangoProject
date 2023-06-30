from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    email=models.CharField(max_length=35)
    phone=models.IntegerField(null=True)
    address=models.CharField(max_length=50)
class Book(models.Model):
    title=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    pdf=models.FileField(upload_to="book/pdf")
    cover=models.ImageField(upload_to="book/image",null=True,blank=True)
class images(models.Model):
    image=models.CharField(max_length=255)
    