from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Ad


class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ["title", "description", "price", "category"]


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email"]
