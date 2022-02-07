from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account (models.Model):
    user_id=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    fname=models.CharField(max_length=20)
    anum=models.IntegerField(max_length=20)
    num=models.IntegerField(max_length=50,default="0")
    email=models.CharField(max_length=40)
    password=models.CharField(max_length=20)
    balance=models.IntegerField(default="100000")
    

