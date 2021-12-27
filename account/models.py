from django.db import models
from django.contrib.auth.models import AbstractUser
from . managers import CustomUserManager
# Create your models here.



class Account(AbstractUser):
    email=models.EmailField(unique=True, blank=None)
    name=models.CharField(max_length=255, blank=None)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    objects=CustomUserManager()