from django.urls import path 
from Apptercera import views
from .views import *


urlpatterns = [
    
    path('', views.inicio, name="Inicio"),
    path('profesores/', views.profesores, name="Profesores"),
    path('estudiantes/', views.estudiantes, name="Estudiantes"),
    path('cursos/', views.cursos, name="Cursos"),
    path('entregables/', views.entregables, name="Entregables"),
    path('Actividades/', views.actividades, name="Actividades"),
    
]
    
    
