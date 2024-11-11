from django import forms
from django.contrib.auth.password_validation import validate_password



class UserForm(forms.Form):
    username = forms.CharField(
        label="Nombre de usuario",
        max_length=140,
    )
    first_name = forms.CharField(
        label="Nombre",
        max_length=140,
    )
    last_name = forms.CharField(
        label="Apellidos",
        max_length=140,
    )
    email = forms.EmailField(
        label="Email",
        max_length=140,
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(),
        label="Contraseña",
        required=True,
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(),
        label="Repite tu contraseña",
        required=True,
    )
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        
        if password1 != password2 and password1 != "":
            raise forms.ValidationError("Las contraseñas no coinciden")
        
        if password2 != "":
            validate_password(password2)
        
        return password2
    
    def clean_nombre(self):
        first_name = self.cleaned_data["first_name"]
        if len(first_name) < 5:
            raise forms.ValidationError("El nombre debe tener al menos 5 caracteres")
        return first_name


