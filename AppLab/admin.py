from django.contrib import admin
from datetime import datetime
from .models import *

# Register your models here.

class TramiteAdmin(admin.ModelAdmin):
    list_display = ['fecha','motivo','estado', 'antiguedad']
    search_fields = ['motivo',]
    list_filter = ['estado',]

    def antiguedad(self, object):

        if object.fecha:
            return (datetime.now().date() - object.fecha).days


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['apellido', 'nombre', 'email']
    search_fields = ['apellido', 'nombre', 'email']


class AgenteAdmin(admin.ModelAdmin):
    list_display = ['apellido', 'nombre', 'funciones', 'email']
    search_fields = ['apellido', 'nombre', 'funciones', 'email']

admin.site.register(Tramite, TramiteAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Agente, AgenteAdmin)