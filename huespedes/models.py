from django.db import models
from django_countries.fields import CountryField
from habitaciones.models import Habitacion

class Persona(models.Model):
    habitacion = models.ForeignKey(Habitacion, related_name='ocupantes', on_delete=models.CASCADE)
    nombre_y_apellido = models.CharField(max_length=70)
    dni_o_pasaporte = models.CharField(max_length=15)
    nacionalidad = CountryField()
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    notas_personas = models.TextField(max_length=500, blank=True)
    ha_ingresado = models.BooleanField(default=False)
    ha_salido = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre_y_apellido

