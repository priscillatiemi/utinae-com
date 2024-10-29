from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Usuário"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Digite sua senha"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Confirmar senha"}))

    class Meta:
        model = User
        fields = ['username', 'email']