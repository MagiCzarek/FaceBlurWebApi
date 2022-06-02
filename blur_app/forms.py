from django import forms
from .models import UploadedFile


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = {'image'}
