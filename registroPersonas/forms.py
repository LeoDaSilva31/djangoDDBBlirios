from django import forms
from .models import Persona

class EditarFechaSalidaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['fecha_salida']
        widgets = {
            'fecha_salida': forms.DateInput(attrs={'type': 'date'}),
        }
