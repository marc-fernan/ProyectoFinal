from django.db import models

# Modelos

class Usuario(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

class Agente(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    funciones = models.CharField(max_length=50)

class Tramite(models.Model):

    motivo = models.CharField(max_length=50)
    fecha = models.DateField()
    estado = models.CharField(max_length=50)