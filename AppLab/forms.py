from django import forms

class TramiteFormulario(forms.Form):

    motivo = forms.CharField()
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    estado = forms.CharField()

class AgenteFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    funciones = forms.CharField(max_length=30)

class UsuarioFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()