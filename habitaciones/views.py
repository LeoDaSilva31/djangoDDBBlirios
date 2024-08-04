from django.shortcuts import render, get_object_or_404, redirect
from .models import Habitacion
from .forms import HabitacionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import dev_login_required


@login_required
@dev_login_required
def crear_habitacion(request):
    if request.method == 'POST':
        form = HabitacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Habitación creada exitosamente.')
            return redirect('listar_habitaciones')
    else:
        form = HabitacionForm()
    return render(request, 'habitacionesTemplates/crear_habitacion.html', {'form': form})

@login_required
@dev_login_required
def listar_habitaciones(request):
    habitaciones = Habitacion.objects.all()
    return render(request, 'habitacionesTemplates/listar_habitaciones.html', {'habitaciones': habitaciones})

@login_required
@dev_login_required
def editar_habitacion(request, habitacion_id):
    habitacion = get_object_or_404(Habitacion, id=habitacion_id)
    if request.method == 'POST':
        form = HabitacionForm(request.POST, instance=habitacion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Habitación actualizada exitosamente.')
            return redirect('listar_habitaciones')
    else:
        form = HabitacionForm(instance=habitacion)
    return render(request, 'habitacionesTemplates/editar_habitacion.html', {'form': form})

@login_required
@dev_login_required
def borrar_habitacion(request, habitacion_id):
    habitacion = get_object_or_404(Habitacion, id=habitacion_id)
    if request.method == 'POST':
        habitacion.delete()
        messages.success(request, 'Habitación eliminada exitosamente.')
        return redirect('listar_habitaciones')
    return redirect('listar_habitaciones')
