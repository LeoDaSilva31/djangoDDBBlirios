from django import forms
from .models import Habitacion

class HabitacionForm(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = ['numero_habitacion', 'nombre_habitacion', 'estado', 'capacidad', 'notas_habitaciones']

