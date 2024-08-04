from django import forms
from .models import Persona
from habitaciones.models import Habitacion

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['habitacion', 'nombre_y_apellido', 'dni_o_pasaporte', 'nacionalidad', 'fecha_entrada', 'fecha_salida', 'notas_personas']

    def __init__(self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)
        self.fields['habitacion'].queryset = Habitacion.objects.filter(estado='libre')

    def clean(self):
        cleaned_data = super().clean()
        fecha_entrada = cleaned_data.get("fecha_entrada")
        fecha_salida = cleaned_data.get("fecha_salida")

        if fecha_entrada and fecha_salida and fecha_salida < fecha_entrada:
            raise forms.ValidationError("La fecha de salida no puede ser anterior a la fecha de entrada.")

        return cleaned_data

