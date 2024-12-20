from django.forms import ModelForm
from .models import Resident
from django import forms

class ResidentForm(ModelForm):
    class Meta:
        model = Resident
        fields = '__all__'
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-field', 'min': '1900-01-01', 'max': '2024-12-31'}),
        }