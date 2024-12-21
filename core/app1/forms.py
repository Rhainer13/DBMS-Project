from django.forms import ModelForm
from .models import Resident, Medicine, MedicineRequest
from django import forms
from datetime import date

class ResidentForm(ModelForm):
    class Meta:
        model = Resident
        fields = '__all__'
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-field', 'min': '1900-01-01', 'max': '2024-12-31'}),
        }

    def __init__(self, *args, **kwargs):
        super(ResidentForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'].initial = '09'

class MedicineForm(ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'
        widgets = {
            'expiry_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-field'}),
        }

    def clean_expiry_date(self):
        expiry_date = self.cleaned_data.get('expiry_date')
        if expiry_date and expiry_date < date.today():
            raise forms.ValidationError("Expiry date cannot be in the past.")
        return expiry_date
    
class MedicineRequestForm(forms.ModelForm):
    class Meta:
        model = MedicineRequest
        fields = ['resident', 'medicine', 'quantity']