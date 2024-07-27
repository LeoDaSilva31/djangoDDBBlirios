from django.urls import path
from .views import editar_fecha_salida, registrar_ingreso, listar_personas, listar_pendientes, listar_salidos, listar_borrados, marcar_salido, marcar_borrado, buscar_persona
from .views import ver_habitaciones, detalles_habitacion

urlpatterns = [
    path('registrarIngreso/', registrar_ingreso, name='registrarIngreso'),
    path('buscarPersona/', buscar_persona, name='buscarPersona'),
    path('listarPersonas/', listar_personas, name='listarPersonas'),
    path('listarPendientes/', listar_pendientes, name='listarPendientes'),
    path('listarSalidos/', listar_salidos, name='listarSalidos'),
    path('listarBorrados/', listar_borrados, name='listarBorrados'),
    path('marcarSalido/<int:persona_id>/', marcar_salido, name='marcar_salido'),
    path('marcarBorrado/<int:persona_id>/', marcar_borrado, name='marcar_borrado'),
    path('ver_habitaciones/', ver_habitaciones, name='ver_habitaciones'),
    path('detalles_habitacion/<int:habitacion_id>/', detalles_habitacion, name='detalles_habitacion'),
    path('editar_fecha_salida/<int:persona_id>/', editar_fecha_salida, name='editar_fecha_salida'),
]



