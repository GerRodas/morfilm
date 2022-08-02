"""morfilm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from morfi.views import algunaspelis, comofunciona, desarroladores, inicio, comentarios, busquedaComida, resultadoBusqueda, cargarComida
from morfi.views import graciasCargaComida, graciasComentario, foro, enDesarrollo


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('inicio.html', inicio),
    path('comofunciona.html', comofunciona),
    path('algunaspelis.html', algunaspelis),
    path('hayequipo.html', desarroladores),
    path('comentarios.html', comentarios, name="comentarios"),
    path('graciasporsumar.html', graciasComentario),
    path('busquedaComida.html', busquedaComida, name="buscar"),
    path('resultadoBusqueda.html',resultadoBusqueda, name="resultado"),
    path('cargarComida.html', cargarComida, name="cargarComida"),
    path('graciasCargaFilm.html', graciasCargaComida),
    path('foro.html', foro),
    path('enDesarrollo.html',enDesarrollo),
]
