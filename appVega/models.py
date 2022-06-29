from distutils.command.upload import upload
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import ImageField

# Create your models here.

class Jugador(models.Model):

    nombre=models.CharField(max_length=40)
    nacionalidad = models.CharField(max_length=20)
    edad=models.IntegerField()
    titulos = models.IntegerField()
    #foto=ImageField(upload_to='appVega/fotos')
    equipo=models.CharField(max_length=40)

def __str__(self):
    return f"Jugador: {self.nombre} - Nacionalidad: {self.nacionalidad} - Edad: {self.edad} - Titulos: {self.titulos} - Equipo: {self.equipo}"# - Equipo: {self.equipo}"

class Equipo(models.Model):

    pais=models.CharField(max_length=20)
    titulos=models.IntegerField()

class Fixture(models.Model):
    pais=models.CharField(max_length=20)
    grupo=models.CharField(max_length=20)
    cabeza_de_serie=models.BooleanField()
