from django import forms
from .models import testModel

class UploadFileForm(forms.Form):
    requestor = forms.CharField(max_length=50)
    file = forms.FileField()