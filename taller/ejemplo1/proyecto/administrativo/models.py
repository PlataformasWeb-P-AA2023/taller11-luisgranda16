from django.db import models

# Create your models here.

class Edificio(models.Model):
    opciones_tipo_edificio = (
        ('Residencial', 'Comercial'),
        ('Comercial', 'Residencial'),
        )

    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30, \
            choices=opciones_tipo_edificio)

    def __str__(self):
        return "%s - tipo: %s" % (self.nombre, 
                                  self.direccion, 
                                  self.ciudad,  
                                  self.tipo)
    
    def obtener_cuartos(self):
        valor = [t.numeroCuartos for t in self.Departamentos.all()]
        valor = sum(valor)
        return valor
    
    def obtener_costos(self):
        valor = [t.costo for t in self.Departamentos.all()]
        valor = sum(valor)
        return valor

class Departamento(models.Model):

    propietario = models.CharField(max_length=30)
    costo = models.IntegerField('costo del departamento')
    numeroCuartos = models.IntegerField('número de cuartos')
    edificio = models.ForeignKey(Edificio, related_name='Departamentos', on_delete=models.CASCADE)

    def __str__(self):
        return "%s | Costos del departamento: %d | Número de cuartos: %d | Edificio: %d"  % (self.propietario,
                                               self.costo,
                                               self.numeroCuartos,
                                               self.edificio)