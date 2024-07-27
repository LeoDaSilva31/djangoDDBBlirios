from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls')),
    path('accounts/', include('allauth.urls')),
    path('registroPersonas/', include('registroPersonas.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]


