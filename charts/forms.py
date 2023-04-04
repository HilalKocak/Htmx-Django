from django import forms
from .models import DataFile

class DataForm(forms.ModelForm):
    class Meta:
        model = DataFile
        fields = ['workingfile']
