from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2'
        ]


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

# class ContactForm(forms.Form):
#     subject = forms.CharField(label='Subject', widget=forms.TextInput(attrs={'class': 'form-control'}))
#     content = forms.CharField(label='Text', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
