from django.forms import ModelForm
from django import forms
from .models import Files


class UploadFileForm(ModelForm):
    class Meta:
        model = Files
        fields = ['title', 'uploadfile']
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        # }
