from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy as _lazy


class ContactForm(forms.Form):
    
    nombre = forms.CharField(
        label=_("Nombre"),
        max_length=100
    )
    email = forms.EmailField(
        label=_("Correo electronico"),
    )
    comentario = forms.CharField(
        label=_("Comentario"),
        max_length= 300,
        widget=forms.Textarea,
    )
    def clean_comentario(self):
        comentario = self.cleaned_data["comentario"]
        if len(comentario) < 5:
            raise forms.ValidationError(_("El comentario debe tener al menos 5 caracteres"))
        return comentario
    
    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        if len(nombre) < 5:
            raise forms.ValidationError(_("El nombre debe tener al menos 5 caracteres"))
        return nombre
    
    
