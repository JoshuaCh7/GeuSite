from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.http import HttpResponse
from django.contrib import messages

def index(request):
    if request.method == "GET":
        return render(request, 'geuSite/index.html')
    #gestion de archivos
def viewGestionArchivo(request):
    if request.method == "GET":
        archivosRegistrados = archivos.objects.all()
        return render(request, 'geuSite/gestionArchivo/gestionArchivo.html',{'archivosRegistrados': archivosRegistrados})

    #gestion de usuarios
def viewGestionUsuario(request):
    if request.method == "GET":
        usuariosRegistrados = archivos.objects.all()
        return render(request, 'geuSite/gestionUsuario/gestionUsuario.html',
                          {'usuariosRegistrados': usuariosRegistrados})

    #plan de formacion
def viewSeccionModulo(request):
    if request.method == "GET":
        return render(request, 'geuSite/planDeFormacion/modulo.html')

def viewSeccionLecciones(request):
    if request.method == "GET":
        return render(request, 'geuSite/planDeFormacion/Lecciones.html')
