from django import forms

class ComentariosFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    email = forms.EmailField()
    asunto = forms.CharField(max_length=30)
    comentario = forms.CharField(max_length=1000)

class ComidaFormulario(forms.Form):
    nombre_comida = forms.CharField(max_length=30)
    pelicula_involucrada = forms.CharField()
    
