from django.db import models
from django_countries.fields import CountryField

class Habitacion(models.Model):
    NOMBRE_HABITACION_CHOICES = [
        ('suite', 'Suite'),
        ('duplex', 'Duplex'),
        ('simple', 'Simple'),
    ]
    ESTADO_CHOICES = [
        ('libre', 'Libre'),
        ('ocupada', 'Ocupada'),
        ('reservada', 'Reservada'),
    ]

    numero_habitacion = models.IntegerField(unique=True, choices=[(i, i) for i in range(1, 46)])
    nombre_habitacion = models.CharField(max_length=20, choices=NOMBRE_HABITACION_CHOICES)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES)
    capacidad = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    notas_habitaciones = models.TextField(max_length=1000, blank=True)
    fecha_entrada = models.DateField(null=True, blank=True)
    fecha_salida = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Habitación {self.numero_habitacion} ({self.nombre_habitacion})"

