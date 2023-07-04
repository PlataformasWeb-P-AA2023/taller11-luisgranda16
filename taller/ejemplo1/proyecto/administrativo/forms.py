from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from administrativo.models import Edificio, Departamento

# Form Edificio
class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad', 'tipo']
        labels = {
            'nombre': _('Ingrese el nombre del edificio'),
            'direccion': _('Ingrese la direccion'),
            'ciudad': _('Ingrese la ciudad'),
            'tipo': _('Ingrese el tipo de edificio'),
        }

    def clean_ciudad(self):
        valor = self.cleaned_data['ciudad']
        num_palabras = valor[0:1]
        
        if num_palabras == "L":
            raise forms.ValidationError("Ingrese una ciudad valida")
        return valor

     
# Form Departamento   
class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['propietario', 'costo', 'numeroCuartos', 'edificio']
        labels = {
            'propietario': _('Ingrese el nombre del propietario'),
            'costo': _('Ingrese el costo'),
            'numeroCuartos': _('Ingrese el numero de cuartos'),
            'edificio': _('Elija el edificio'),
        }
    
    def clean_numeroCuartos(self):
        valor = self.cleaned_data['numeroCuartos']
        if (valor) == 0 or (valor) > 7:
            raise forms.ValidationError("Ingrese un numero de cuartos no mayor a 7")
        return valor
    
    def clean_costo(self):
        valor = self.cleaned_data['costo']
        if (valor) > 100000:
            raise forms.ValidationError("Ingrese un costo valido")
        return valor

    def clean_propietario(self):
        valor = self.cleaned_data['propietario']
        num_palabras = len(valor.split())

        if num_palabras < 3:
            raise forms.ValidationError("Ingrese sus nombres y apellidos")
        return valor
    