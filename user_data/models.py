from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser

# Create your models here.

class user_detail(models.Model):
    email=models.EmailField(max_length=240,unique=True)
    fname=models.CharField(max_length=250)
    lname=models.CharField(max_length=250)
    contact=models.CharField(max_length=10)
    # img=models.ImageField(upload_to="img",default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users_id=models.ForeignKey(User,on_delete=models.CASCADE,blank=True)


class Address(models.Model):
    house_no=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    Country=models.CharField(max_length=50)
    users_id=models.ForeignKey(user_detail,on_delete=models.CASCADE)
    is_primary = models.BooleanField(default=False)

class ai_data(models.Model):
    name=models.CharField(max_length=50)
    openai_model=models.CharField(max_length=50)
    key=models.CharField(max_length=255,default="",null=True)
    users_id=models.ForeignKey(User,on_delete=models.CASCADE)



    
