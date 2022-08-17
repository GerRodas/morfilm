from django.contrib import admin
from morfi.models import Avatar, Usuario, Comentarios, Cargar_pelicula, Comida
# Register your models here.

class Usuarioadmin(admin.ModelAdmin):
    list_display = ["nombre", "apellido", "edad", "nacimiento"]
    search_fields = ["nombre", "apellido", "edad", "nacimiento"]

class Comentariosadmin(admin.ModelAdmin):
    list_display = ["nombre", "email", "asunto", "comentario"]
    search_fields = ["nombre", "email", "asunto", "comentario"]

class Cargar_peliculaadmin(admin.ModelAdmin):
    list_display = ["nombre_film", "comidas_involucradas"]
    search_fields = ["nombre_film", "comidas_involucradas"]

class Comidaadmin(admin.ModelAdmin):
    list_display = ["nombreComida", "nombrePelicula"]
    search_fields = ["nombreComida", "nombrePelicula"]

admin.site.register(Usuario, Usuarioadmin)
admin.site.register(Comentarios, Comentariosadmin)
admin.site.register(Cargar_pelicula, Cargar_peliculaadmin)
admin.site.register(Comida, Comidaadmin)
admin.site.register(Avatar)
