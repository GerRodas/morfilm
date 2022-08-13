from email.mime import image
from operator import mod
from django.db import models


# Create your models here.

class Usuario(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    nacimiento = models.DateField()

    #DEBERIAMOS PLANTEAR CAMBIAR LOS MODELS DE USUARIO Y COMENTARIO. SE PUEDEN COMPLEMENTAR. QUE EL USUARIO TENGA
    # NOMBRE, APELLIDO, EDAD, EMAIL

    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.edad} - {self.nacimiento}"

class Comentarios(models.Model):

    nombre = models.CharField( max_length=50)
    email = models.EmailField(max_length=254)
    asunto = models.CharField(max_length=50)
    comentario = models.CharField(max_length=1000)

    #COMO PARA COMENTAR, EL USUARIO TIENE QUE ESTAR LOGUEADO, PODEMOS CITAR DATOS DEL USUARIO, COMO NOMBRE Y ALGUNA
    #OTRA COSA MÁS. 

    def __str__(self):
        return f"{self.nombre} - {self.email} - {self.asunto} - {self.comentario}"

class Cargar_pelicula(models.Model):

    nombre_film = models.CharField(max_length=50)
    comidas_involucradas = models.CharField(max_length=50)
    anio_film = models.IntegerField()
    imagen_film = models.ImageField()
    imagen_comida = models.ImageField()
    descripcion_film = models.CharField(max_length=300)
    tiempo_comen_film = models.TimeField()

    #AGREGAR IMAGEN DE LA PELI INVOLUCRADA DONDE COMEN ESO (LA IMAGEN EXACTA SERÍA GENIAL)
    #OTROS OBJETOS USABLES SERÍAN: AÑO FILM, TIEMPO DONDE COMEN ESO, GENERO DE LA PELICULA
    

    def __str__(self):
        return f"{self.nombre_film} - {self.comidas_involucradas}"

class Comida(models.Model):

    nombreComida = models.CharField(max_length=50)
    nombrePelicula = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.nombreComida} - {self.nombrePelicula}"