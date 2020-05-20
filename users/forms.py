from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Profile
from django import forms

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Adres email')
    username = forms.CharField(label='Nazwa użytkownika')
    password1 = forms.CharField(label='Hasło')
    password2 = forms.CharField(label='Powtórz hasło')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    username = forms.CharField(label='Nazwa')
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField(label='Zdjęcie profilowe')
    class Meta:
        model = Profile
        fields = ['image']

