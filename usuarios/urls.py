from django.urls import path
from .views import bienvenida, custom_login, custom_logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('bienvenida/', bienvenida, name='bienvenida'),
    path('', custom_login, name='custom_login'),
    path('logout/', custom_logout, name='custom_logout'),
]
