from django.db import models

# Create your models here.

class Edificio(models.Model):
    opciones_tipo_edificio = (
        ('residencial', 'Comercial'),
        ('comercial', 'residencial'),
        )

    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30, \
            choices=opciones_tipo_edificio)
    Edificio = models.ForeignKey(Departamento, related_name='Departamentoss', on_delete=models.CASCADE)

    def __str__(self):
        return "%s - tipo: %s" % (self.nombre, 
                                  self.direccion, 
                                  self.ciudad, 
                                  self.tipo)

class Departamento(models.Model):

    nombreCompleto = models.CharField(max_length=30)
    costo = models.IntegerField('costo del departamento')
    numeroCuartos = models.IntegerField('número de cuartos')
    edificios = models.IntegerField('numero de edificios')
    Departamento = models.ForeignKey(Edificio, related_name='Edificioss', on_delete=models.CASCADE)

    def __str__(self):
        return "%s | Costos del departamento: %d | Número de cuartos: %d | : %d"  % (self.nombre,
                                               self.viviendas,
                                               self.num_parques,
                                               self.edificios)