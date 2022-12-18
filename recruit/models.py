from turtle import position
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Internship(models.Model):
    category = models.CharField(max_length=100,default=" ")
    name = models.CharField(max_length=100)
    desc = models.TextField()
    stipend = models.FloatField(default=0.0)
    img = models.ImageField(upload_to="pics")
    date = models.DateField()
    duration = models.IntegerField(default=6)
    position = models.CharField(max_length=100)
  
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phno = models.CharField(default=0,max_length=10)
    tell_me = models.TextField()
    address = models.TextField()
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    zip = models.CharField(default=0,max_length=6)
  
    def __str__(self):
        return self.fname
    
class Resume(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=0)
    resume_file = models.FileField(upload_to="pics")
    
    def __str__(self):
        return str(self.user)
    
    
