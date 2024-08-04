# urls.py de losLirios principal
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls')),
    path('habitaciones/', include('habitaciones.urls')),
    path('huespedes/', include('huespedes.urls')),  
    path('accounts/', include('allauth.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]


