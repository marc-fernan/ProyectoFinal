from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from AppLab.models import *
from AppLab.forms import TramiteFormulario

# Vistas!

def inicio(req):
    return render(req, "AppLab/inicio.html")

def usuarios(req):
    return render(req, "AppLab/usuarios.html")

def agentes(req):
    return render(req, "AppLab/agentes.html")

def tramites(req):
    return render (req, "AppLab/tramites.html")

def padre(req):
    return render(req, "AppLab/padre.html")

def tramiteFormulario(req):
    print('method', req.method)
    print('POST', req.POST)
    if req.method == "POST":
            tramiteFormulario = TramiteFormulario(req.POST) # Aqui me llega la informacion del html
             
            if tramiteFormulario.is_valid():
                  informacion = tramiteFormulario.cleaned_data
                  tramite = Tramite(motivo=informacion["motivo"], fecha=informacion["fecha"], estado=informacion["estado"])
                  tramite.save()
                  return render(req, "AppLab/inicio.html")
    else:
            tramiteFormulario = TramiteFormulario()
            return render(req, "AppLab/tramiteFormulario.html", {"tramiteFormulario": tramiteFormulario})



