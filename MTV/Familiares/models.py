from django.db import models

# Create your models here.
class FamiliaresModel(models.Model):
    nombre=models.CharField(max_length=25)
    edad=models.IntegerField()
    nacimiento=models.DateField()
