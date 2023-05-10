from django.db import models

# Create your models here.

class User(models.Model):
    f_name = models.CharField(max_length=150)
    l_name = models.CharField(max_length=150)
    mobile = models.IntegerField()

