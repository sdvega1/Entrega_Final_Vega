from distutils.command.upload import upload
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import ImageField
from django.contrib.auth.models import User

# Create your models here.

class Jugador(models.Model):

    nombre=models.CharField(max_length=40)
    nacionalidad = models.CharField(max_length=20)
    edad=models.IntegerField()
    titulos = models.IntegerField()
    #foto=ImageField(upload_to='appVega/fotos')
    equipo=models.CharField(max_length=40)

    def __str__(self):
        return f"Nombre: {self.nombre} - Nacionalidad: {self.nacionalidad} - Edad: {self.edad} - Titulos: {self.titulos} - Equipo: {self.equipo}"# - Equipo: {self.equipo}"

class Equipo(models.Model):

    pais=models.CharField(max_length=20)
    titulos=models.IntegerField()

    def __str__(self):
        return f"Pais: {self.pais} - Titulos: {self.titulos}"

class Fixture(models.Model):
    pais=models.CharField(max_length=20)
    grupo=models.CharField(max_length=20)
    cabeza_de_serie=models.BooleanField()

    def __str__(self):
        return f"Pais: {self.pais} - Grupo: {self.grupo} - Cabeza de Serie: {self.cabeza_de_serie}"

class Blog(models.Model):
    nombre=models.CharField(max_length=20)
    titulo=models.CharField(max_length=30)
    fecha=models.DateField()
    cuerpo=models.CharField(max_length=500)

    def __str__(self):
        return f"Nombre: {self.nombre} - Titulo: {self.titulo} - Fecha: {self.fecha} - Cuerpo: {self.cuerpo}"

class Avatar(models.Model):
    #vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #subcarpeta avatares media
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)