from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from .models import *
from .forms import *

# Vistas!

def inicio(req):
    return render(req, "AppLab/inicio.html")

def busquedaTramite(req):
    lista = Tramite.objects.all()
    return render(req, "AppLab/busquedaTramite.html", {"busquedaTramite": lista})

def buscarTramite(req: HttpRequest):

    if req.GET["motivo"]:
        motivo = req.GET["motivo"]
        tramite = Tramite.objects.filter(motivo__icontains=motivo)
        return render(req, "AppLab/resultadoBusqueda.html", {"tramite": tramite})

def usuarios(req):
    return render(req, "AppLab/usuarios.html")

def agentes(req):
    return render(req, "AppLab/agentes.html")

def tramites(req):
    return render (req, "AppLab/tramites.html")

def padre(req):
    return render(req, "AppLab/padre.html")

def tramiteFormulario(req):
    
    if req.method == 'POST':
            tramiteFormulario = TramiteFormulario(req.POST) # Aqui me llega la informacion del html
             
            if tramiteFormulario.is_valid():
                  informacion = tramiteFormulario.cleaned_data
                  tramite = Tramite(motivo=informacion["motivo"], fecha=informacion["fecha"], estado=informacion["estado"])
                  tramite.save()
                  return render(req, "AppLab/inicio.html")
    else:
            tramiteFormulario = TramiteFormulario()
            return render(req, "AppLab/tramiteFormulario.html", {"tramiteFormulario": tramiteFormulario})
    
def usuarioFormulario(req):
    
    if req.method == 'POST':
            usuarioFormulario = UsuarioFormulario(req.POST) # Aqui me llega la informacion del html
             
            if usuarioFormulario.is_valid():
                  informacion = usuarioFormulario.cleaned_data
                  usuario = Usuario(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"])
                  usuario.save()
                  return render(req, "AppLab/inicio.html")
    else:
            usuarioFormulario = UsuarioFormulario()
            return render(req, "AppLab/usuarioFormulario.html", {"usuarioFormulario": usuarioFormulario})

def agenteFormulario(req):
    
    if req.method == 'POST':
            agenteFormulario = AgenteFormulario(req.POST) # Aqui me llega la informacion del html
             
            if agenteFormulario.is_valid():
                  informacion = agenteFormulario.cleaned_data
                  agente = Agente(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], funciones=informacion["funciones"])
                  agente.save()
                  return render(req, "AppLab/inicio.html")
    else:
            agenteFormulario = AgenteFormulario()
            return render(req, "AppLab/agenteFormulario.html", {"agenteFormulario": agenteFormulario})

