from django import forms
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext as _
from django.shortcuts import render,redirect
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    username = forms.CharField(
        label=_("Nombre de usuario"),
        max_length=140,
        required=True
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label=_("Contraseña")
    ) 
    


class UserRegisterForm(forms.Form):
    username = forms.CharField(
        label=_("Nombre de usuario"),
        max_length=140,
    )
    first_name = forms.CharField(
        label=_("Nombre"),
        max_length=140,
    )
    Last_name = forms.CharField(
        label=_("Apellidos"),
        max_length=140,
    )
    email = forms.EmailField(
        label=_("Email"),
        max_length=140,
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(),
        label=_("Contraseña"),
        required=True,
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(),
        label=_("Repite tu contraseña"),
        required=True,
    )
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        
        if password1 != password2 and password1 != "":
            raise forms.ValidationError(_("Las contraseñas no coinciden"))
        
        if password2 != "":
            validate_password(password2)
        
        return password2
    
    def clean_nombre(self):
        first_name = self.cleaned_data["first_name"]
        if len(first_name) < 5:
            raise forms.ValidationError(_("El nombre debe tener al menos 5 caracteres"))
        return first_name

def registro_view(request):
    if request.POST:
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data["username"]
            first_name = formulario.cleaned_data["first_name"]
            last_name = formulario.cleaned_data["Last_name"]
            email = formulario.cleaned_data["email"]
            password1 = formulario.cleaned_data["password1"]
            password2 = formulario.cleaned_data["password2"]
            user =User.objects.create_user(username,email,password2)
            if user: 
                user.first_name = first_name
                user.last_name = last_name
                user.password1 = password1
                user.save()
                
            context = {
                "msg" : _("Usuario creado correctamente"),
                
            }
            return render(request,'general/registro.html', context)
        
        else:
            context = {
                "form" : formulario,
            }
            return render(request,'general/registro.html', context)
    else:
        formulario = UserRegisterForm()
        context = {
            "form" : formulario
            }
        return render(request,'general/registro.html', context)

        

