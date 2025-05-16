from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User1(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=24)
    email=models.EmailField()
    dob=models.DateField()
    phone=models.IntegerField(max_length=11)
    last_login = models.DateTimeField(blank=True, null=True)
    