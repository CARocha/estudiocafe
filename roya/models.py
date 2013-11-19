# -*- coding: utf-8 -*-

from django.db import models
from encuesta.models import Encuesta

# Create your models here.
# 5.1
class Impactos(models.Model):
    nombre = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = 'Impactoss'

    def __unicode__(self):
        return self.nombre

class ImpactoRoya(models.Model):
    impacto = models.ForeignKey(Impactos)
    doce = models.FloatField('2011-12')
    trece = models.FloatField('2012-13')
    catorce = models.FloatField('2013-14')

    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = '5.1 Impacto de la roya en la finca'

    def __unicode__(self):
        pass

#5.2
class TipoCafetos(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Tipo Cafetos'

    def __unicode__(self):
        return self.nombre

class PodaCafetos(models.Model):
    tipo_2012 = models.ForeignKey(TipoCafetos, related_name="tipo_2012", 
                            verbose_name=u'¿Qué tipo? Antes de crisis 2011-12')
    tipo_2014 = models.ForeignKey(TipoCafetos, related_name="tipo_2014", 
                            verbose_name=u'¿Qué tipo? Después de crisis 2013-14')
    mz_2012 = models.FloatField('¿Cuántas mz 2011-12?')
    mz_2014 = models.FloatField('¿Cuántas mz 2013-14?')

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = '5.2-a Manejo: Poda de cafetos'

    def __unicode__(self):
        pass

class RecepoCafetos(models.Model):
    mz_2012 = models.FloatField('¿Cuántas mz 2011-12?')
    mz_2014 = models.FloatField('¿Cuántas mz 2013-14?')

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = '5.2-b Manejo: Recepo de cafetos'

    def __unicode__(self):
        pass

class TipoVariedad(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Variedades de Renovación'

    def __unicode__(self):
        return self.nombre

class RenovacionCafetales(models.Model):
    tipo_2012 = models.ForeignKey(TipoVariedad, related_name="tipo_2012", 
                            verbose_name=u'¿Qué tipo? Antes de crisis 2011-12')
    tipo_2014 = models.ForeignKey(TipoVariedad, related_name="tipo_2014", 
                            verbose_name=u'¿Qué tipo? Después de crisis 2013-14')
    mz_2012 = models.FloatField('¿Cuántas mz 2011-12?')
    mz_2014 = models.FloatField('¿Cuántas mz 2013-14?')

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = '5.2-c Renovación de cafetales'

    def __unicode__(self):
        pass

class TipoSombra(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Tipos de sombra'

    def __unicode__(self):
        return self.nombre

class ManejoSombra(models.Model):
    tipo_2012 = models.ForeignKey(TipoSombra, related_name="tipo_2012", 
                            verbose_name=u'¿Qué tipo? Antes de crisis 2011-12')
    tipo_2014 = models.ForeignKey(TipoSombra, related_name="tipo_2014", 
                            verbose_name=u'¿Qué tipo? Después de crisis 2013-14')
    mz_2012 = models.FloatField('¿Cuántas mz 2011-12?')
    mz_2014 = models.FloatField('¿Cuántas mz 2013-14?')

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = '5.2-d Manejo de sombra'

    def __unicode__(self):
        pass

class Fertilizacion(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Tipos Fertilización'

    def __unicode__(self):
        return self.nombre

class ManejoFertilizacion(models.Model):
    tipo_2012 = models.ForeignKey(Fertilizacion, related_name="tipo_2012", 
                            verbose_name=u'¿Qué tipo? Antes de crisis 2011-12')
    tipo_2014 = models.ForeignKey(Fertilizacion, related_name="tipo_2014", 
                            verbose_name=u'¿Qué tipo? Después de crisis 2013-14')
    mz_2012 = models.FloatField('¿Cantidad de plantas 2011-12?')
    mz_2014 = models.FloatField('¿Cantidad de plantas  2013-14?')

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = '5.2-e Fertilización'

    def __unicode__(self):
        pass

class TipoAplicacionFungicida(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Tipos aplicación fungicidas'

    def __unicode__(self):
        return self.nombre

class AplicacionFungicida(models.Model):
    tipo_2012 = models.ForeignKey(TipoAplicacionFungicida, related_name="tipo_2012", 
                            verbose_name=u'¿Qué tipo? Antes de crisis 2011-12')
    tipo_2014 = models.ForeignKey(TipoAplicacionFungicida, related_name="tipo_2014", 
                            verbose_name=u'¿Qué tipo? Después de crisis 2013-14')
    mz_2012 = models.FloatField('¿Cuántas aplicaciones? 2011-12?')
    mz_2014 = models.FloatField('¿Cuántas aplicaciones?  2013-14?')
    dosis_2012 = models.FloatField('¿Qué dosis? 2011-12?')
    dosis_2014 = models.FloatField('¿Qué dosis?  2013-14?')

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = '5.2-f Aplicación de fungicida'

    def __unicode__(self):
        pass

#5.3
class Combatir(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
       
        verbose_name_plural = 'Combatir'

    def __unicode__(self):
        return self.nombre

class Oriento(models.Model):
    opcion = models.ManyToManyField(Combatir, related_name="opcion")

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = '5.3 ¿ Quién le orientó sobre como combatir la roya?'

    def __unicode__(self):
        pass
    
#5.4
class Productos(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Productos'

    def __unicode__(self):
        return self.nombre

class NuevosProductos(models.Model):
    producto = models.ForeignKey(Productos)
    frecuencia = models.FloatField('Frecuencia de aplicación')
    cantidad = models.FloatField('Cantidad por manzana')

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = '5.4 ¿Que nuevos productos usan ahora para combatir la roya?'

    def __unicode__(self):
        pass

#5.5
class AdelanteTipoCafetos(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Tipo Cafetos'

    def __unicode__(self):
        return self.nombre

class AdelantePodaCafetos(models.Model):
    tipo_2016 = models.ForeignKey(AdelanteTipoCafetos, related_name="adelante_tipo_2016", 
                            verbose_name=u'¿Qué tipo?  2014-16')
    mz_2016 = models.FloatField('¿Cuántas mz 2014-16?')

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = '5.5-a Manejo: Poda de cafetos'

    def __unicode__(self):
        pass

class AdelanteRecepoCafetos(models.Model):
    mz_2016 = models.FloatField('¿Cuántas mz 2014-16?')

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = '5.5-b Manejo: Recepo de cafetos'

    def __unicode__(self):
        pass

class AdelanteTipoVariedad(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Variedades de Renovación'

    def __unicode__(self):
        return self.nombre

class AdelanteRenovacionCafetales(models.Model):
    tipo_2016 = models.ForeignKey(AdelanteTipoVariedad, related_name="adelante_tipo_2016", 
                            verbose_name=u'¿Qué tipo? 2014-16')
    mz_2016 = models.FloatField('¿Cuántas mz 2014-16?')
   

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = '5.5-c Renovación de cafetales'

    def __unicode__(self):
        pass

class AdelanteTipoSombra(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Tipos de sombra'

    def __unicode__(self):
        return self.nombre

class AdelanteManejoSombra(models.Model):
    tipo_2016 = models.ForeignKey(TipoSombra, related_name="adelante_tipo_2016", 
                            verbose_name=u'¿Qué tipo? Antes de crisis 2011-12')
    mz_2016 = models.FloatField('¿Cuántas mz 2011-12?')

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = '5.5-d Manejo de sombra'

    def __unicode__(self):
        pass

class AdelanteFertilizacion(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Tipos Fertilización'

    def __unicode__(self):
        return self.nombre

class AdelanteManejoFertilizacion(models.Model):
    tipo_2016 = models.ForeignKey(Fertilizacion, related_name="adelante_tipo_2016", 
                            verbose_name=u'¿Qué tipo? 2014-16')
    mz_2016 = models.FloatField('¿Cantidad de plantas 2014-16?')

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = '5.5-e Fertilización'

    def __unicode__(self):
        pass

class AdelanteTipoAplicacionFungicida(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Tipos aplicación fungicidas'

    def __unicode__(self):
        return self.nombre

class AdelanteAplicacionFungicida(models.Model):
    tipo_2016 = models.ForeignKey(TipoAplicacionFungicida, related_name="adelante_tipo_2016", 
                            verbose_name=u'¿Qué tipo? 2014-16')
    mz_2016 = models.FloatField('¿Cuántas aplicaciones? 2014-16?')
    dosis_2016 = models.FloatField('¿Qué dosis? 2014-16?')
    
    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = '5.5-f Aplicación de fungicida'

    def __unicode__(self):
        pass

#5.6
CHOICES_NIVEL = (
            (1, 'Igual'),
            (2, 'Menos'),
            (3, 'Más'),
    )

CHOICES_VARIEDAD = (
            (1, 'Las mismas'),
            (2, 'Otras'),
            (3, 'No se'),
    )
CHOICES_FINCA = (
            (1, 'Si'),
            (2, 'No'),
            (3, 'No se'),
    )

class Igual(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Igual'

    def __unicode__(self):
        return self.nombre

class Mas(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Mas'

    def __unicode__(self):
        return self.nombre
    
class Menos(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Menos'

    def __unicode__(self):
        return self.nombre

class Variedades(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Variedades'

    def __unicode__(self):
        return self.nombre

class NivelFinca(models.Model):
    area = models.IntegerField('Area de cafe ', choices=CHOICES_NIVEL)
    variedades = models.IntegerField('Variedades de café', choices=CHOICES_VARIEDAD)
    cuales = models.ManyToManyField(Variedades, related_name="cuales",
                                verbose_name=u'Cuales serán las otras variedades')
    produccion = models.IntegerField('La producción de café', choices=CHOICES_NIVEL)
    igual = models.ForeignKey(Igual, verbose_name=u'Porqué igual')
    mas = models.ForeignKey(Mas, verbose_name=u'Porqué más')
    menos = models.ForeignKey(Menos, verbose_name=u'Porqué menos')
    otros_productos = models.IntegerField('Habrá otros productos que repondrá el café o se cultivará junto al café', 
                                                                choices=CHOICES_FINCA)
    respuesta = models.TextField('Si la respuesta es si, cuales y porque', null=True, blank=True)

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = '5.6 A nivel de la finca de aqui a 5-10 años'

    def __unicode__(self):
        pass

#5.6-2 Capacitaciones técnica recibida
class TipoCapacitaciones(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Tipo Capacitaciones'

    def __unicode__(self):
        return self.nombre

class Capacitor(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Capacitor'

    def __unicode__(self):
        return self.nombre

CHOICES_GRATIS = (
            (1, 'Gratis'),
            (2, 'Pago'),
    )
CHOICES_NIVEL_CONOCIMIENTO = (
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
    )

class Metodologia(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Metodología'

    def __unicode__(self):
        return self.nombre

class CapacitacionesTecnicas(models.Model):
    tipo = models.ForeignKey(TipoCapacitaciones)
    cuantas = models.IntegerField('2013¿Cuántas veces?')
    profesor = models.ForeignKey(Capacitor)
    gratis = models.IntegerField(choices=CHOICES_GRATIS)
    metodologia = models.ManyToManyField(Metodologia, related_name="metodologia",
                                    verbose_name=u'¿Qué metodología utilizarón?')
    nivel = models.IntegerField(choices=CHOICES_NIVEL_CONOCIMIENTO, null=True, blank=True)

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = '5.6 Capacitaciones técnica recibida'

    def __unicode__(self):
        pass

#5.7
class TemasSociales(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Temas Sociales'

    def __unicode__(self):
        return self.nombre

class CapacitacionesSociales(models.Model):
    tipo = models.ForeignKey(TemasSociales)
    cuantas = models.IntegerField('2013¿Cuántas veces?')
    profesor = models.ForeignKey(Capacitor)
    gratis = models.IntegerField(choices=CHOICES_GRATIS)
    metodologia = models.ManyToManyField(Metodologia, 
                                        related_name="capacitacion_metodologia",
                                        verbose_name=u'¿Qué metodología utilizarón?')
    nivel = models.IntegerField(choices=CHOICES_NIVEL_CONOCIMIENTO, null=True, blank=True)

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = '5.7 Capacitaciones en tema social recibidas'

    def __unicode__(self):
        pass

#5.8
class SiLeGusta(models.Model):
    metodologia = models.ManyToManyField(Metodologia, related_name="si_metodologia",
                                verbose_name=u'¿Qué metodología de capacitación le gusto más a usted?')
    porque = models.TextField()

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = '¿Qué metodología de capacitación le gusto más a usted?'

    def __unicode__(self):
        pass

class NoLeGusta(models.Model):
    metodologia = models.ManyToManyField(Metodologia, related_name="no_metodologia",
                                verbose_name=u' Qué metodología de capacitación le gusto menos a usted?')
    porque = models.TextField()

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = ' Qué metodología de capacitación le gusto menos a usted?'

    def __unicode__(self):
        pass

#5.9
class Plantio(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Plantio'
        verbose_name_plural = 'Plantios'

    def __unicode__(self):
        return self.nombre

CHOICES_TIPOS_PLANTA = (
            (1, 'D'),
            (2, 'P'),
            (3, 'R'),
    )
CHOICES_VARIEDAD_PROD = (
            (1, 'C'),
            (2, 'CT'),
            (3, 'CM'),
            (4, 'B'),
            (5, 'P'),
            (6, 'H'),
    )
CHOICES_TIPO_SOMBRA = (
            (1, 'SM'),
            (2, 'SVS'),
            (3, 'SG'),
            (4, 'SS'),
    )
class TipoFertilizacion(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Tipo Fertilizacion'

    def __unicode__(self):
        return self.nombre

class TipoFungicida(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Tipo Fungicida'

    def __unicode__(self):
        return self.nombre

class DetalleIncidenciaRoya(models.Model):
    plantio = models.ForeignKey(Plantio)
    area = models.FloatField('Area en MZ')
    planta = models.IntegerField('Tipo de plantas', choices=CHOICES_TIPOS_PLANTA)
    edad = models.FloatField('Edad en años')
    variedad = models.IntegerField('Variedades Predominante', choices=CHOICES_VARIEDAD_PROD)
    sombra = models.IntegerField('Tipo de Sombra', choices=CHOICES_TIPO_SOMBRA)
    nivel = models.FloatField('Nivel de sombra%')
    fertilizacion = models.ManyToManyField(TipoFertilizacion, related_name="fertilizante",
                                    verbose_name=u'Tipo de fertilización')
    dosis = models.FloatField('Dosis de fertilizaciónOnza/ pl QLibras/ pl O')
    fungicidas = models.ManyToManyField(TipoFungicida, related_name="fungicida",
                                        verbose_name=u'Tipo de fungicidas')
    aplicaciones = models.FloatField('Número de aplicaciones por año')
    afectadas = models.FloatField('% de plantas afectadas con Roya')
    hojas = models.FloatField('% de hojas afectadas con Roya')

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = 'Detalles de incidencia de roya en algunos plantíos'

    def __unicode__(self):
        pass