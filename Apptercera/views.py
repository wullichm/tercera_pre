from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse
from Apptercera.models import *

# Create your views here.

def inicio(request):
    return render(request, 'Apptercera/index.html')
    # return HttpResponse('Vista Inicio')

def profesores(request):
    return render(request, 'Apptercera/profesores.html')

def estudiantes(request):
    return render(request, 'Apptercera/estudiantes.html')

def cursos(request):

    cursos = Curso.object.all()

    return render(request, 'Apptercera/cursos.html')

def entregables(request):
    return render(request, 'Apptercera/entregables.html')

def actividades(request):
    return render(request, 'Apptercera/actividades.html')