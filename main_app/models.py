from django.db import models

# Create your models here.

class Plant(models.Model):
  name = models.CharField(max_length=100)
  species = models.CharField(max_length=100)
  care = models.TextField(max_length=250)

def __str__(self):
    return self.name 