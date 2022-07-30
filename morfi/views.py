
from django.http import HttpResponse
from django.shortcuts import render

from morfi.models import Comentarios
from morfi.forms import ComentariosFormulario
from morfi.models import Comida

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


def resultadoComida(request):
 

    if request.GET["nombreComida"]:

        comida = request.GET["nombreComida"]

        pelicula = Comida(comida__icontains=comida)

        return render(request, "resultadoBusqueda.html", {"nombreComida": comida, "peli": pelicula})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)