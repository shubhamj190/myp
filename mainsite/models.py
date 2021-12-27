from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    contact = models.CharField(max_length=10)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    
    def __str__(self):
        return self.email

class Projects(models.Model):
    image = models.ImageField(upload_to='media/')