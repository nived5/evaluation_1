from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_workmanager = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)

class user(models.Model):
    user = models.ForeignKey(Login,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)

class workmanager(models.Model):
    user = models.ForeignKey(Login,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email =  models.EmailField(max_length=100)
