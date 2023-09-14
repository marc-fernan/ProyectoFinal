from django.urls import path
from AppLab import views

urlpatterns = [
    path('inicio/', views.inicio),
    path('usuarios/', views.usuarios, name="usuarios"),
    path('agentes/', views.agentes, name="agentes"),
    path('tramites/', views.tramites, name="tramites"),
    path('padre', views.padre, name="padre"),
    path('tramiteFormulario/', views.tramiteFormulario, name="tramiteFormulario")
]