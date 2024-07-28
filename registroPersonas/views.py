from datetime import datetime
from django.utils import timezone
from django.shortcuts import get_object_or_404, render, redirect
from .models import Persona, Habitacion
from django_countries import countries

from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Persona, Habitacion
from django_countries import countries
from django.contrib.auth.decorators import login_required


@login_required
def registrar_ingreso(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        dni_o_pasaporte = request.POST['dni_o_pasaporte']
        fecha_entrada = request.POST['fecha_entrada']
        numero_habitacion_id = request.POST['numero_habitacion']
        nacionalidad = request.POST['nacionalidad']

        numero_habitacion = Habitacion.objects.get(id=numero_habitacion_id)

        nueva_persona = Persona(
            nombre=nombre,
            apellido=apellido,
            dni_o_pasaporte=dni_o_pasaporte,
            fecha_entrada=fecha_entrada,
            numero_habitacion=numero_habitacion,
            nacionalidad=nacionalidad
        )
        nueva_persona.save()

        # Actualizar la habitación para reflejar que ya no está libre
        numero_habitacion.datos_personas[nueva_persona.dni_o_pasaporte] = {
            "nombre": nombre,
            "apellido": apellido,
            "fecha_entrada": fecha_entrada,
            "nacionalidad": nacionalidad
        }
        numero_habitacion.actualizar_estado()

        return redirect('listarPersonas')

    habitaciones = Habitacion.objects.all()
    return render(request, 'registroPersonas/registrarIngreso.html', {
        'habitaciones': habitaciones,
        'countries': list(countries)
    })


@login_required
def listar_pendientes(request):
    pendientes = Persona.objects.filter(pendiente=True).order_by('-fecha_entrada')
    return render(request, 'registroPersonas/listarPendientes.html', {'pendientes': pendientes})

@login_required
def listar_salidos(request):
    salidos = Persona.objects.filter(salio=True).order_by('-fecha_entrada')
    return render(request, 'registroPersonas/listarSalidos.html', {'salidos': salidos})

@login_required
def listar_personas(request):
    personas = Persona.objects.all().order_by('-fecha_entrada')
    return render(request, 'registroPersonas/listarPersonas.html', {'personas': personas})


@login_required
def marcar_salido(request, persona_id):
    persona = Persona.objects.get(id=persona_id)
    persona.marcar_salido()
    return redirect('listarPendientes')

from django.shortcuts import render, redirect, get_object_or_404
from .models import Persona
from django.utils import timezone

@login_required
def listar_borrados(request):
    borrados = Persona.objects.filter(fecha_eliminacion__isnull=False)
    return render(request, 'registroPersonas/listarBorrados.html', {'borrados': borrados})

@login_required
def marcar_borrado(request, persona_id):
    persona = get_object_or_404(Persona, id=persona_id)
    persona.fecha_eliminacion = timezone.now()
    persona.usuario_responsable = request.user
    persona.save()
    return redirect('listarBorrados')

@login_required
def buscar_persona(request):
    query = request.GET.get('q', '')
    personas = Persona.objects.filter(fecha_eliminacion__isnull=True).filter(
        nombre__icontains=query
    ) | Persona.objects.filter(fecha_eliminacion__isnull=True).filter(
        apellido__icontains=query
    ) | Persona.objects.filter(fecha_eliminacion__isnull=True).filter(
        dni_o_pasaporte__icontains=query
    ) | Persona.objects.filter(fecha_eliminacion__isnull=True).filter(
        nacionalidad__icontains=query
    )
    return render(request, 'registroPersonas/buscarPersona.html', {'personas': personas, 'query': query})

@login_required
def ver_habitaciones(request):
    habitaciones = Habitacion.objects.all()
    for habitacion in habitaciones:
        habitacion.esta_ocupada = Persona.objects.filter(numero_habitacion=habitacion, pendiente=True).exists()
    return render(request, 'registroPersonas/ver_habitaciones.html', {'habitaciones': habitaciones})

def detalles_habitacion(request, habitacion_id):
    habitacion = get_object_or_404(Habitacion, id=habitacion_id)
    personas = Persona.objects.filter(numero_habitacion=habitacion, pendiente=True).order_by('-fecha_entrada')
    habitaciones = Habitacion.objects.all()
    for hab in habitaciones:
        hab.esta_ocupada = Persona.objects.filter(numero_habitacion=hab, pendiente=True).exists()
    return render(request, 'registroPersonas/detalles_habitacion.html', {
        'habitacion': habitacion,
        'personas': personas,
        'habitaciones': habitaciones
    })

from .forms import EditarFechaSalidaForm

@login_required
def editar_fecha_salida(request, persona_id):
    persona = get_object_or_404(Persona, id=persona_id)
    if request.method == 'POST':
        if 'marcar_salida' in request.POST:
            persona.fecha_salida = timezone.now().date()
            persona.salio = True
            persona.pendiente = False
            persona.save()
            return redirect('detalles_habitacion', habitacion_id=persona.numero_habitacion.id)
        else:
            form = EditarFechaSalidaForm(request.POST, instance=persona)
            if form.is_valid():
                form.save()
                return redirect('detalles_habitacion', habitacion_id=persona.numero_habitacion.id)
    else:
        form = EditarFechaSalidaForm(instance=persona)
    return render(request, 'registroPersonas/editar_fecha_salida.html', {'form': form, 'persona': persona})