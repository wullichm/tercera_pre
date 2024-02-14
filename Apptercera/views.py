from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse
from Apptercera.models import *
from Apptercera.forms import *

# Create your views here.

def inicio(request):

    if request.method == 'POST':
        miFormulario = Buscar(request.POST)
                
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data

            curso = Curso.objects.filter(nombre__icontains=info["nombre"])

            return render(request, "Apptercera/index.html", {"cursos": curso})
        
    else:
        miFormulario = Buscar()

    return render(request, "Apptercera/index.html", {"Formulario": miFormulario})

def profesores(request):
     
    if request.method == 'POST':

        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data
            profe = Profesores(nombre=informacion["nombre"],apellido=informacion["apellido"],email=informacion["email"])
            profe.save()
            return render(request,"Apptercera/index.html")
         
    else:
        miFormulario= ProfesorFormulario()
    return render(request,"Apptercera/profesores.html",{"Formulario": miFormulario})

def estudiantes(request):
     
    if request.method == 'POST':
        miFormularioE = EstudiantesFormulario(request.POST)
        print(miFormularioE)

        if miFormularioE.is_valid():
            informacion = miFormularioE.cleaned_data
            estud = Estudiantes(nombre=informacion["nombre"],apellido=informacion["apellido"],email=informacion["email"])
            estud.save()
            return render(request,"Apptercera/index.html")
    else:
        miFormularioE= EstudiantesFormulario()
    return render(request,"Apptercera/estudiantes.html",{"FormularioE": miFormularioE})

def cursos(request):

    if request.method == 'POST':
        miFormularioC = CursosFormulario(request.POST)
        print(miFormularioC)

        if miFormularioC.is_valid():
            informacion = miFormularioC.cleaned_data
            curs = Curso(nombre=informacion["nombre"],camada=informacion["camada"])
            curs.save()
            return render(request,"Apptercera/index.html")
    else:
        miFormularioC= CursosFormulario()
    return render(request,"Apptercera/cursos.html",{"FormularioC": miFormularioC})


def entregables(request):
 
    if request.method == 'POST':
        miFormularioE = EntregablesFormulario(request.POST)
        print(miFormularioE)

        if miFormularioE.is_valid():
            informacion = miFormularioE.cleaned_data
            entre = Entregables(nombre=informacion["nombre"],trabajo=informacion["trabajo"],fecha=informacion["fecha"],entregado=informacion["entregado"])
            entre.save()
            return render(request,"Apptercera/index.html")
    else:
        miFormularioE= EntregablesFormulario()
    return render(request,"Apptercera/entregables.html",{"FormularioE": miFormularioE})


def actividades(request):
 
    if request.method == 'POST':
        miFormularioA = ActividadesFormularios(request.POST)
        print(miFormularioA)

        if miFormularioA.is_valid():
            informacion = miFormularioA.cleaned_data
            acti = Extracurricular(nombre=informacion["nombre"],apellido=informacion["apellido"],actividad=informacion["actividad"])
            acti.save()
            return render(request,"Apptercera/index.html")
    else:
        miFormularioA= ActividadesFormularios()
    return render(request,"Apptercera/actividades.html",{"FormularioA": miFormularioA})

def base(request):
    return render(request, 'Apptercera/base.html')

def buscar(request):

    if request.method == 'POST':
        miFormulario = Buscar(request.POST)
                
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data

            curso = Curso.objects.filter(nombre__icontains=info["nombre"])

            return render(request, "Apptercera/buscar.html", {"cursos": curso})
        
    else:
        miFormulario = Buscar()

    return render(request, "Apptercera/buscar.html", {"Formulario": miFormulario})