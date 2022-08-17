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
from atexit import register
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path

from morfi.views import algunaspelis, comofunciona, desarroladores, inicio, comentarios, busquedaComida, loginView, resultadoBusqueda, cargarComida, register, solo_staff, editar_perfil, agregar_avatar
from morfi.views import graciasCargaComida, graciasComentario, foro, enDesarrollo

from django.contrib.auth.views import LogoutView

# 13-08
from django.conf import settings
from django.conf.urls.static import static

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
    path("login", loginView, name="login"),
    path("registrar", register, name="registrar"),
    path("logout", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("solostaff", solo_staff, name= "solostaff"),
    path("editarperfil", editar_perfil, name="EditarPerfil"),
    path("avatar", agregar_avatar, name="avatar")

    
]

#13-08
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)