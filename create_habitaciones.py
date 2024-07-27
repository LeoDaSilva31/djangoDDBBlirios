from registroPersonas.models import Habitacion

for i in range(1, 21):
    if not Habitacion.objects.filter(numero_habitacion=i).exists():
        Habitacion.objects.create(numero_habitacion=i)
