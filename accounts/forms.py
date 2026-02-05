import re
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User


class RegisterForm(UserCreationForm):
    image = forms.ImageField(allow_empty_file=True, required=False)
    bio = forms.CharField(max_length=150, required=False)
    class Meta:
        model = User
        fields = ("username", "email", "bio", "image")


class CustomUserChangeForm(UserChangeForm):
    image = forms.ImageField(allow_empty_file=True)
    bio = forms.CharField(
        max_length=150, widget=forms.TextInput(attrs={"required": False})
    )

    class Meta:
        model = User
        fields = ("username", "email", "bio", "image")
