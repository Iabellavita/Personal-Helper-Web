from django.forms import ModelForm
from django import forms
from .models import Files


# from .file_valid import FileValidator
#
# content_types = ['application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'image/jpeg', 'image/png',
#                  'application/pdf', 'application/msword', 'text/plain']
#
# validate_file = FileValidator(max_size=1024 * 10,
#                               content_types=(content_types,))


class UploadFileForm(ModelForm):
    class Meta:
        model = Files
        fields = ['title', 'uploadfile']
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        # }
