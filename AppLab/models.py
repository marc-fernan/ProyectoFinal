from django.db import models

# Modelos

class Usuario(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}'
    
    class Meta():

        ordering = ('nombre',)

class Agente(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    funciones = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido} - {self.funciones}'

class Tramite(models.Model):

    motivo = models.CharField(max_length=50)
    fecha = models.DateField()
    estado = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f'Motivo: {self.motivo} - Estado: {self.estado}'