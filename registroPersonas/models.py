from django.db import models
from django.shortcuts import get_object_or_404, render
from django_countries.fields import CountryField
from django.utils import timezone
from django.contrib.auth.models import User

class Habitacion(models.Model):
    numero_habitacion = models.IntegerField(unique=True)
    datos_personas = models.JSONField(default=dict)
    libre = models.BooleanField(default=True)

    def actualizar_estado(self):
        self.libre = not Persona.objects.filter(numero_habitacion=self, pendiente=True).exists()
        self.save()

    def __str__(self):
        return f'Habitación {self.numero_habitacion}'

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni_o_pasaporte = models.CharField(max_length=50, unique=True)
    fecha_entrada = models.DateField(default=timezone.now)
    fecha_salida = models.DateField(null=True, blank=True)
    numero_habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    nacionalidad = CountryField(blank_label='(select country)')
    borrado = models.BooleanField(default=False)
    salio = models.BooleanField(default=False)
    pendiente = models.BooleanField(default=True)
    fecha_eliminacion = models.DateTimeField(null=True, blank=True)
    usuario_responsable = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def marcar_salido(self):
        self.salio = True
        self.pendiente = False
        self.save()

    def marcar_borrado(self):
        self.borrado = True
        self.salio = True  # Marcar también como salio
        self.pendiente = False
        self.fecha_eliminacion = timezone.now()
        self.save()

    def __str__(self):
        return f'{self.nombre} {self.apellido} ({self.dni_o_pasaporte})'

def ver_habitaciones(request):
    habitaciones = Habitacion.objects.all()
    for habitacion in habitaciones:
        # Comprobar si hay personas pendientes en la habitación
        habitacion.esta_ocupada = Persona.objects.filter(numero_habitacion=habitacion, estado='pendiente').exists()
    return render(request, 'registroPersonas/ver_habitaciones.html', {'habitaciones': habitaciones})

def detalles_habitacion(request, habitacion_id):
    habitacion = get_object_or_404(Habitacion, id=habitacion_id)
    personas = Persona.objects.filter(numero_habitacion=habitacion, estado='pendiente')
    habitaciones = Habitacion.objects.all()
    for hab in habitaciones:
        hab.esta_ocupada = Persona.objects.filter(numero_habitacion=hab, estado='pendiente').exists()
    return render(request, 'registroPersonas/detalles_habitacion.html', {
        'habitacion': habitacion,
        'personas': personas,
        'habitaciones': habitaciones
    })