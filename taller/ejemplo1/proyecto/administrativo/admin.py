from django.contrib import admin

# Importar las clases del modelo
from administrativo.models import Edificio, Departamento


class EdificioAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'direccion', 'ciudad','tipo')
    search_fields = ('nombre', 'direccion')

admin.site.register(Edificio, EdificioAdmin)

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'propietario', 'costo', 'numeroCuartos', 'edificio')
    search_fields = ('edificio',)

admin.site.register(Departamento, DepartamentoAdmin)