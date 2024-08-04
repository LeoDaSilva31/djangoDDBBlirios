from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_huespedes, name='registrar_huespedes'),
    path('listar/', views.listar_huespedes, name='listar_huespedes'),
    path('get_capacidad/', views.get_capacidad, name='get_capacidad'),
    path('presentes/', views.huespedes_presentes, name='huespedes_presentes'),
    path('liberar/<int:habitacion_id>/', views.liberar_habitacion, name='liberar_habitacion'),
    path('reservas/calendario/', views.calendario_reservas, name='calendario_reservas'),
]

