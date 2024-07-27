from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('bienvenida')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos')
    return render(request, 'usuariosTemplates/base.html')

@login_required
def bienvenida(request):
    return render(request, 'usuariosTemplates/bienvenida.html')

def custom_logout(request):
    logout(request)
    return render(request, 'usuariosTemplates/hastaLuego.html')