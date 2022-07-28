from email.mime import image
from multiprocessing.pool import MapResult
from operator import mod
from django.db import models
from django.forms import ImageField

# Create your models here.


class Usuario(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    nacimiento = models.DateField()

class Comentarios(models.Model):

    titulo = models.CharField( max_length=50)
    comentario = models.CharField(max_length=1000)

class Cargar_pelicula(models.Model):

    nombre_film = models.CharField(max_length=50)
    comidas_involucradas = models.CharField(max_length=50)