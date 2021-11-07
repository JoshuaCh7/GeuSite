from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),

    #Gestion de archivos
    path('viewGestionArchivo', views.viewGestionArchivo, name='viewGestionArchivo'),

    #Gestion de usuarios
    path('viewGestionUsuario', views.viewGestionUsuario, name='viewGestionUsuario'),

    #Plan de formacion
    path('viewSeccionModulo', views.viewSeccionModulo, name='viewSeccionModulo'),
    path('viewSeccionLecciones', views.viewSeccionLecciones, name='viewSeccionLecciones'),
]