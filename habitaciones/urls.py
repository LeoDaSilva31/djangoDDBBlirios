from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_habitacion, name='crear_habitacion'),
    path('listar/', views.listar_habitaciones, name='listar_habitaciones'),
    path('editar/<int:habitacion_id>/', views.editar_habitacion, name='editar_habitacion'),
    path('borrar/<int:habitacion_id>/', views.borrar_habitacion, name='borrar_habitacion'),
]

