from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('usuarios/', usuarios, name="usuarios"),
    path('agentes/', agentes, name="agentes"),
    path('tramites/', tramites, name="tramites"),
    path('padre', padre, name="padre"),
    path('tramiteFormulario/', tramiteFormulario, name="tramiteFormulario"),
    path('usuarioFormulario/', usuarioFormulario, name="usuarioFormulario"),
    path('agenteFormulario/', agenteFormulario, name="agenteFormulario")
]