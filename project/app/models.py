from django.db import models

# Create your models here.
class users(models.Model):
    username=models.TextField()
    email=models.TextField()
    password=models.TextField()


class files(models.Model):
    file=models.FileField()
   

