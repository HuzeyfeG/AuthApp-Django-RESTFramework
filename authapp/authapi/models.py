from django.db import models

# Create your models here.

class SignUpModel(models.Model):
    username = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

class LogInModel(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)