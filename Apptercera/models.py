from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

class Entregables(models.Model):
    nombre = models.CharField(max_length=40)
    trabajo = models.CharField(max_length=40)
    fecha = models.DateField()
    entregado = models.BooleanField()

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

class Profesores(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    
class Extracurricular(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    actividad = models.CharField(max_length=20)