from django import forms
from django.forms import ModelForm
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy as _lazy
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from posts.models import Comments

class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = [ 
            "text",
            ]
