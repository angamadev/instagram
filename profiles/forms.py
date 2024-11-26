from django import forms

class ProfileFollow(forms.Form):
    profile_pk = forms.IntegerField(label="Identificador de usuario",widget=forms.HiddenInput())