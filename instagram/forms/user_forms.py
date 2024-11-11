from django import forms
from django.forms import ModelForm
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy as _lazy
from django.shortcuts import render,redirect
from django.contrib.auth.models import User

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = [   
            "username",
            "first_name",
            "email",
            "password",
            ]
    def save(self):
        user = super().save(commit=True)
        user.set_password(self.cleaned_data["password"])
        user.save()

        from profiles.models import UserProfile
        UserProfile.objects.create(user=user)

        return user

# class LoginForm(forms.Form):
#     username = forms.CharField(
#         label=_("Nombre de usuario"),
#         max_length=140,
#         required=True
#     )
#     password = forms.CharField(
#         widget=forms.PasswordInput(),
#         label=_("Contraseña")
#     ) 



# # def registro_view(request):
#     if request.POST:
#         formulario = UserRegisterForm(request.POST)
#         if formulario.is_valid():
#             username = formulario.cleaned_data["username"]
#             first_name = formulario.cleaned_data["first_name"]
#             last_name = formulario.cleaned_data["Last_name"]
#             email = formulario.cleaned_data["email"]
#             password1 = formulario.cleaned_data["password1"]
#             password2 = formulario.cleaned_data["password2"]
#             user =User.objects.create_user(username,email,password2)
#             if user: 
#                 user.first_name = first_name
#                 user.last_name = last_name
#                 user.password1 = password1
#                 user.save()
                
#             context = {
#                 "msg" : _("Usuario creado correctamente"),
                
#             }
#             return render(request,'general/registro.html', context)
        
#         else:
#             context = {
#                 "form" : formulario,
#             }
#             return render(request,'general/registro.html', context)
#     else:
#         formulario = UserRegisterForm()
#         context = {
#             "form" : formulario
#             }
#         return render(request,'general/registro.html', context)

