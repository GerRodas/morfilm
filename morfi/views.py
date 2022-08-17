
from re import A
from django.http import HttpResponse
from django.shortcuts import render

from morfi.models import Avatar, Comentarios, Cargar_pelicula, Comida
from morfi.forms import ComentariosFormulario, ComidaFormulario, UserEditform, AvatarFormulario

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required

from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth.models import User


# Create your views here.



def inicio(request):

    try:
       avatar = Avatar.objects.get(user=request.user.id)
       return render(request, "inicio.html", {"url": avatar.imagen.url})

    except:
        return render(request, "inicio.html")

    
def comofunciona(self):
    return render(self, "comofunciona.html")

def algunaspelis(self):
    return render(self, "algunaspelis.html")

def desarroladores(self):
    return render(self, "hayequipo.html")

@login_required
def comentarios(request):

    if request.method == "POST":

        miFormulario = ComentariosFormulario(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            comments = Comentarios(nombre=data['nombre'], email=data['email'], asunto=data['asunto'], comentario=data['comentario'],)

            comments.save()

            return render(request, 'graciasComentarios.html')

    else:

        miFormulario = ComentariosFormulario()
    
    return render(request, "comentarios.html", {"miFormulario": miFormulario})

def graciasComentario(request):

    return render(request, 'graciasComentarios.html')


def busquedaComida(request):

    return render(request, 'busquedaComida.html')


@staff_member_required(login_url="solostaff")
def cargarComida(request):

    if request.method == "POST":

        miComida = ComidaFormulario(request.POST)

        if miComida.is_valid():

            data = miComida.cleaned_data

            food = Cargar_pelicula(nombre_film=data['pelicula_involucrada'], comidas_involucradas=data['nombre_comida'])

            food.save()

            return render(request, 'graciasCargaFilm.html')
    else:

        miComida = ComidaFormulario()
    
    return render(request, "cargarComida.html", {"miComida": miComida})

def graciasCargaComida(request):

    return render(request, 'graciasCargaFilm.html')

def resultadoBusqueda(request):

    if request.GET["nombreComida"]:

        comida = request.GET["nombreComida"]

        pelicula = Cargar_pelicula.objects.filter(comidas_involucradas__icontains=comida)

        return render(request, "resultadoBusquedaPro.html", {"nombreComida": comida, "nombre_film": pelicula})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)


def foro(request):

    if request.GET:
        
        nombre, comentario = Comentarios.objects.all

        return render(request, "foro.html", {"nombre": nombre, "comentario": comentario})

    else:

        respuesta = "No hay comentarios para mostrar"

    return HttpResponse(respuesta)


def enDesarrollo(request):

    return render(request, 'enDesarrollo.html')


#DOMINGO 7/8 DIEGO LOGIN, LOGOUT, REGISTRO

def loginView(request):

    if request.method == "POST":

        miFormulario = AuthenticationForm(request, data=request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            usuario = data["username"]
            psw = data["password"]

            user = authenticate(username=usuario, password=psw)

            if user:

                login(request, user)

                return render(request, "loginfalse.html", {"mensaje": f"Bienvendido {usuario}"})

            else:

                return render (request, "loginfalse.html", {"mensaje": "Error, datos incorrectos"})
        
        return render (request, "loginfalse.html", {"mensaje": "Error, datos incorrectos"})
        
    else:

        miFormulario = AuthenticationForm()

    return render(request, "login.html", {"miFormulario": miFormulario})




def register(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]

            form.save()

            return render(request, "loginfalse.html", {"mensaje": f"Usuario {username} creado"})
    
    else:

        form = UserCreationForm()

    return render(request, "registro.html", {"miFormulario": form})




def solo_staff(self):
    return render(self, "solostaff.html")


#DIEGO  13-08
@login_required
def editar_perfil(request):

    usuario = request.user

    if request.method == "POST":
        
        miFormulario = UserEditform(request.POST, instance=request.user)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]

            usuario.save()
#HACER TEMPLATE QUE INFORME DATOS INGRESADOS CORRECTAMENTE
            return render(request, "editarperfilok.html")

    else:

        miFormulario = UserEditform(instance=request.user)

    return render(request, "editarPerfil.html", {"miFormulario": miFormulario})



@login_required
def agregar_avatar(request):

    if request.method == "POST":
        
        miFormulario = AvatarFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():
            #esta parte la arme como la filminas
            u = User.objects.get(username=request.user)
            avatar = Avatar(user=u, imagen=miFormulario.cleaned_data["imagen"])

            #avatar = Avatar(user=request.user, imagen=data['imagen'])

            avatar.save()

        return render(request, "inicio.html")

    else:

        miFormulario = AvatarFormulario()

    return render(request, "agregarAvatar.html", {"miFormulario": miFormulario})