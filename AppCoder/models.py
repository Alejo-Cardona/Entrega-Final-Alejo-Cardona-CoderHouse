from distutils.command.upload import upload
from django.db import models



# Create your models here.
class Auto(models.Model):

    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    motor = models.IntegerField()

    def __str__(self):
        return f'{self.marca} , {self.modelo}'
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self):
        return f'{self.nombre}, {self.apellido}'


class Empleado (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    encargo = models.CharField(max_length=30)
    def __str__(self):
        return f'{self.nombre}, {self.apellido}'





    
    