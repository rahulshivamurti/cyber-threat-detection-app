# cyber/forms.py
from django import forms
from .models import CyberLog
class CyberLogForm(forms.ModelForm):
    class Meta:
        model = CyberLog
        fields = ['log']
