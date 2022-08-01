
from django.http import HttpResponse
from django.shortcuts import render

from morfi.models import Comentarios, Cargar_pelicula, Comida
from morfi.forms import ComentariosFormulario, ComidaFormulario

# Create your views here.



def inicio(self):
    return render(self, "inicio.html")

def comofunciona(self):
    return render(self, "comofunciona.html")

def algunaspelis(self):
    return render(self, "algunaspelis.html")

def desarroladores(self):
    return render(self, "hayequipo.html")

def comentarios(request):

    if request.method == "POST":

        miFormulario = ComentariosFormulario(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            comments = Comentarios(nombre=data['nombre'], email=data['email'], asunto=data['asunto'], comentario=data['comentario'],)

            comments.save()

            return render(request, 'inicio.html')

    else:

        miFormulario = ComentariosFormulario()
    
    return render(request, "comentarios.html", {"miFormulario": miFormulario})


def busquedaComida(request):

    return render(request, 'busquedaComida.html')



def cargarComida(request):

    if request.method == "POST":

        miComida = ComidaFormulario(request.POST)

        if miComida.is_valid():

            data = miComida.cleaned_data

            food = Cargar_pelicula(nombre_film=data['pelicula_involucrada'], comidas_involucradas=data['nombre_comida'])

            food.save()

            return render(request, 'inicio.html')
    else:

        miComida = ComidaFormulario()
    
    return render(request, "cargarComida.html", {"miComida": miComida})



def resultadoBusqueda(request):

    if request.GET["nombreComida"]:

        comida = request.GET["nombreComida"]

        pelicula = Cargar_pelicula.objects.filter(comidas_involucradas__icontains=comida)

        return render(request, "resultadoBusqueda.html", {"nombreComida": comida, "nombre_film": pelicula})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)
