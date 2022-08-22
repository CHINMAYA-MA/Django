from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()


