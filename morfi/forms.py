from django import forms

from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

from .models import Avatar

class ComentariosFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    email = forms.EmailField()
    asunto = forms.CharField(max_length=30)
    comentario = forms.CharField(max_length=1000)

class ComidaFormulario(forms.Form):
    nombre_comida = forms.CharField(max_length=30)
    pelicula_involucrada = forms.CharField()

# AGREGADO 13-08

class UserEditform(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Reingrese contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]

    def clean_password2(self):

        password2 = self.cleaned_data["password2"]
        if password2 != self.cleaned_data["password1"]:
            raise forms.ValidationError("Contraseñas diferentes")
        return password2



class AvatarFormulario(forms.ModelForm):

    class Meta:
        model=Avatar
        fields=('imagen',)
    
