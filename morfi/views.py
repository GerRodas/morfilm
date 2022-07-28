from urllib import request
from django.shortcuts import render

from morfi.models import Comentarios

# Create your views here.



def inicio(self):
    return render(self, "inicio.html")

def comofunciona(self):
    return render(self, "comofunciona.html")

def algunaspelis(self):
    return render(self, "algunaspelis.html")

def desarroladores(self):
    return render(self, "hayequipo.html")

def sugerinos(self):

    if request.method == "POST":
        nombre = Comentarios(nombre = request.POST["nombre"])

    return render(self, "sugerencias.html")