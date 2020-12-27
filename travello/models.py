from django.db import models

# Create your models here.
class Destination(models.Model):

    percent = models.IntegerField()
    name = models.CharField(max_length=100)
    fillvalue = models.CharField(max_length=100)
