# -*- coding: utf-8 -*-

from django.db import models
from encuesta.models import Encuesta, CHOICE_SI_NO

#2.1
class Uso(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Uso de tierra"

class UsoTierra(models.Model):
    ''' Uso de tierra
    '''
    tierra = models.ForeignKey(Uso, verbose_name="Uso de Tierra", 
        null=True, blank=True)
    area = models.FloatField('Área en Mz', null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
        
    class Meta:
        verbose_name_plural = "2.1 Uso de la tierra en la finca"

#2.2
class Actividad(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Actividades de reforestacion"

class Reforestacion(models.Model):
    reforestacion = models.ForeignKey(Actividad, verbose_name="Actividades de reforestación")
    respuesta = models.IntegerField(choices=CHOICE_SI_NO, null=True, blank=True)

    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.reforestacion.nombre
    
    class Meta:
        verbose_name_plural = "2.2 Conservación de recursos naturales en la finca (ciclo de 12 meses)"

#2.3
class Animales(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Animales"

class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    unidad = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Productos"

class ProductosPatio(models.Model):
    nombre = models.CharField(max_length=100)
    unidad = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Productos patios"


class AnimalesFinca(models.Model):
    animales = models.ForeignKey(Animales)
    cantidad = models.FloatField(null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.animales.nombre
    
    class Meta:
        verbose_name_plural = "2.3 Animales en la finca y producción (ciclo de 12 meses)"

class ProductoFinca(models.Model):
    cultivo = models.ForeignKey(Productos, null=True, blank=True)
    area = models.FloatField('Area en Mz',null=True, blank=True)
    total_produccion = models.FloatField('Total producion por año', null=True, blank=True)
    consumo = models.FloatField('Consumo por año', null=True, blank=True)
    venta = models.FloatField('Venta por año', null=True, blank=True)
    
    encuesta = models.ForeignKey(Encuesta)

    class Meta:

        verbose_name_plural = '2.4 Cultivos en la finca y producción (ciclo de ultimo 12 meses)'

    def __unicode__(self):
        pass

class ProductoPatio(models.Model):
    cultivo = models.ForeignKey(ProductosPatio, null=True, blank=True)
    cantidad = models.FloatField('Cantidad de plantas',null=True, blank=True)
    total_produccion = models.FloatField('Total producion por año', null=True, blank=True)
    consumo = models.FloatField('Consumo por año', null=True, blank=True)
    venta = models.FloatField('Venta por año', null=True, blank=True)
    
    encuesta = models.ForeignKey(Encuesta)

    class Meta:

        verbose_name_plural = '2.4-b Cultivos de patio en la finca y producción (ciclo de ultimo 12 meses)'

    def __unicode__(self):
        pass

#2.5
CHOICE_VENDIO = ((1, (u'Comunidad')),
                 (2, (u'Intermediario')),
                 (3, (u'Mercado')),
                 (4, (u'Cooperativa')),
                 (5, (u'Todos'))
                 )


CHOICE_MANEJA = ((1, (u'Hombre')),
                 (2, (u'Mujer')),
                 (3, (u'Ambos')),
                 (4, (u'Hijos/as')),
                 (5, (u'Hombre-Hijos')),
                 (6, (u'Mujer-Hijos')),
                 (7, (u'Todos'))
                 )
                 
CHOICE_CATEG = (
                 (1, u'Agroforestales'),
                 (2, u'Forestales'),
                 (3, u'Granos básicos'),
                 (4, u'Ganado mayor'),
                 (5, u'Animales de patio'),
                 (6, u'Hortalizas y frutas'),
                 (7, u'Musaceas'),
                 (8, u'Raíces y tubérculos')
                     
                )

class Rubros(models.Model):
    nombre = models.CharField(max_length=100)
    unidad = models.CharField(max_length=100)
    categoria = models.IntegerField(choices=CHOICE_CATEG, null = True, blank = True)
    
    def __unicode__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = "Rubros"

class IngresoFamiliar(models.Model):
    ''' Modelo Ingreso familiar. venta de rubros
    '''
    rubro = models.ForeignKey(Rubros)
    cantidad = models.FloatField('Cantidad vendida en el año pasado',
        null=True, blank=True)
    precio = models.FloatField('Precio de venta por unidad(C$ por unidad)',
        null=True, blank=True)
    quien_vendio = models.IntegerField('¿A quien vendio?', choices=CHOICE_VENDIO,
        null=True, blank=True)
    maneja_negocio = models.IntegerField('¿Quién maneja el negocio', choices=CHOICE_MANEJA,
        null=True, blank=True)
    
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.rubro.nombre
    
    class Meta:
        verbose_name_plural = "2.5 Ingreso familiar en efectivo. Venta de rubros (ciclo de 12 meses)"

#2.6
class Fuentes(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Otros-Ingreso - Fuentes"

class TipoTrabajo(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Otro-Ingreso - TipoTrabajo"
      
class OtrosIngresos(models.Model):
    '''Otros ingresos
    '''
    fuente = models.ForeignKey(Fuentes)
    tipo = models.ForeignKey(TipoTrabajo, null=True, blank=True)
    meses = models.IntegerField('# Meses',null=True, blank=True)
    ingreso = models.IntegerField('Ingreso por mes',null=True, blank=True)
    tiene_ingreso = models.IntegerField(choices=CHOICE_MANEJA,null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.fuente.nombre
    
    class Meta:
        verbose_name_plural = "2.6- Otros ingresos (período de referencia últimos 12 meses)"

