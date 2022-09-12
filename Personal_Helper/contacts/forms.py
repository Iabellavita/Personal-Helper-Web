from django import forms
from django.forms import ModelForm

from .models import *


BIRTH_YEAR_CHOICES = [str(year) for year in range(1960, date.today().year)]


class ContactForm(ModelForm):
    name = forms.CharField(label='Contact name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    birthday = forms.DateField(required=False, label='Birthday', widget=forms.SelectDateWidget(empty_label=None, years=BIRTH_YEAR_CHOICES))
    email = forms.EmailField(empty_value=None, required=False, label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    email_one = forms.EmailField(empty_value=None, required=False, label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='Phone', widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_one = forms.CharField(empty_value=None, required=False, label='Phone', widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(required=False, label='Address', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Contacts
        fields = ['name', 'address', 'birthday', 'phone', 'phone_one', 'email', 'email_one']


