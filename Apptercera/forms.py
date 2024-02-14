from django import forms

class ProfesorFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()

class EstudiantesFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()

class CursosFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()

class EntregablesFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    trabajo = forms.CharField(max_length=40)
    fecha = forms.DateField()
    entregado = forms.BooleanField()

class ActividadesFormularios(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=20)
    actividad = forms.CharField(max_length=20)

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=30)