from datetime import date
import json
from django.shortcuts import render, redirect
from .forms import PersonaForm
from .models import Persona
from django.contrib import messages
from habitaciones.models import Habitacion
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from habitaciones.models import Habitacion


@login_required
def registrar_huespedes(request):
    if request.method == 'POST':
        print("Formulario recibido con datos:", request.POST)  # Debug: Verificar datos recibidos
        habitacion = Habitacion.objects.get(id=request.POST.get('habitacion'))
        
        # Convertir fechas al formato esperado por Django
        fecha_entrada = datetime.strptime(request.POST.get('fecha_entrada'), '%d-%m-%Y').strftime('%Y-%m-%d')
        fecha_salida = datetime.strptime(request.POST.get('fecha_salida'), '%d-%m-%Y').strftime('%Y-%m-%d')
        
        notas_personas = request.POST.get('notas_personas')

        registros_exitosos = True

        for i in range(habitacion.capacidad):
            nombre_y_apellido = request.POST.get(f'nombre_y_apellido_{i}')
            dni_o_pasaporte = request.POST.get(f'dni_o_pasaporte_{i}')
            nacionalidad = request.POST.get(f'nacionalidad_{i}')

            print(f"Procesando persona {i}: {nombre_y_apellido}, {dni_o_pasaporte}, {nacionalidad}")  # Debug: Información de la persona

            if nombre_y_apellido and dni_o_pasaporte and nacionalidad:
                nueva_persona = Persona(
                    habitacion=habitacion,
                    nombre_y_apellido=nombre_y_apellido,
                    dni_o_pasaporte=dni_o_pasaporte,
                    nacionalidad=nacionalidad,
                    fecha_entrada=fecha_entrada,
                    fecha_salida=fecha_salida,
                    notas_personas=notas_personas
                )
                nueva_persona.save()
                print(f"Persona {i} guardada correctamente")  # Debug: Confirmación de guardado
            else:
                registros_exitosos = False
                print(f"Error al procesar persona {i}: Datos faltantes")  # Debug: Error de datos faltantes
                break

        if registros_exitosos:
            habitacion.estado = 'ocupada'
            habitacion.save()
            print("Estado de la habitación cambiado a 'ocupada'")  # Debug: Confirmación de cambio de estado
            messages.success(request, 'Huéspedes registrados exitosamente y habitación marcada como ocupada.')
            return redirect('listar_huespedes')
        else:
            messages.error(request, 'Todos los campos de las personas son obligatorios. Por favor, revise los datos ingresados.')
            form = PersonaForm(request.POST)
            return render(request, 'huespedesTemplates/registrar_huespedes.html', {'form': form})

    else:
        print("Mostrando formulario vacío")  # Debug: Indicar que se está mostrando un formulario vacío
        form = PersonaForm()

    return render(request, 'huespedesTemplates/registrar_huespedes.html', {'form': form})

@login_required
def listar_huespedes(request):
    huespedes = Persona.objects.all()
    return render(request, 'huespedesTemplates/listar_huespedes.html', {'huespedes': huespedes})

@login_required
def get_capacidad(request):
    habitacion_id = request.GET.get('habitacion_id')
    if habitacion_id:
        habitacion = Habitacion.objects.get(id=habitacion_id)
        return JsonResponse({'capacidad': habitacion.capacidad})
    return JsonResponse({'capacidad': 0})

@login_required
def huespedes_presentes(request):
    today = date.today()
    presentes = Persona.objects.filter(fecha_salida__gte=today, ha_salido=False)
    agrupados_por_habitacion = {}
    for huesped in presentes:
        if huesped.habitacion not in agrupados_por_habitacion:
            agrupados_por_habitacion[huesped.habitacion] = []
        agrupados_por_habitacion[huesped.habitacion].append(huesped)

    mensaje = "No hay huéspedes registrados en el día de la fecha" if not presentes.exists() else ""

    return render(request, 'huespedesTemplates/huespedes_presentes.html', {
        'agrupados_por_habitacion': agrupados_por_habitacion,
        'mensaje': mensaje
    })

@login_required
def liberar_habitacion(request, habitacion_id):
    habitacion = Habitacion.objects.get(id=habitacion_id)
    personas = Persona.objects.filter(habitacion=habitacion, ha_salido=False)

    # Marcar a todos los huéspedes como que han salido
    for persona in personas:
        persona.ha_salido = True
        persona.save()

    # Cambiar el estado de la habitación a 'libre'
    habitacion.estado = 'libre'
    habitacion.save()

    return redirect('huespedes_presentes')

@login_required
def calendario_reservas(request):
    habitaciones = Habitacion.objects.all()
    eventos = []

    for habitacion in habitaciones:
        if habitacion.fecha_entrada and habitacion.fecha_salida:
            eventos.append({
                'title': f'Habitación {habitacion.numero_habitacion} ({habitacion.estado})',
                'start': habitacion.fecha_entrada.strftime('%Y-%m-%dT%H:%M:%S'),
                'end': habitacion.fecha_salida.strftime('%Y-%m-%dT%H:%M:%S'),
                'color': 'green' if habitacion.estado == 'libre' else 'red'
            })

    print(eventos)  # Imprime los eventos para depuración

    return render(request, 'huespedesTemplates/calendario_reservas.html', {
        'eventos': json.dumps(eventos)
    })
