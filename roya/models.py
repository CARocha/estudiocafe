# -*- coding: utf-8 -*-

from django.db import models
from encuesta.models import Encuesta
from sorl.thumbnail import ImageField
from estudiocafe.utils import get_file_path

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
    doce = models.FloatField('2011-12',null=True, blank=True)
    trece = models.FloatField('2012-13',null=True, blank=True)
    catorce = models.FloatField('2013-14',null=True, blank=True)

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
                            verbose_name=u'¿Qué tipo? Antes de crisis ',
                            null=True, blank=True)
    tipo_2014 = models.ForeignKey(TipoCafetos, related_name="tipo_2014", 
                            verbose_name=u'¿Qué tipo? Después de crisis ',
                            null=True, blank=True)
    #mz_2012 = models.FloatField('¿Cuántas mz 2011-12?',
     #   null=True, blank=True)
    #mz_2014 = models.FloatField('¿Cuántas mz 2013-14?',
      #  null=True, blank=True)

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = '5.2-a Manejo: Poda de cafetos'

    def __unicode__(self):
        pass

class VariedadRecepo(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Variedad recepos'

    def __unicode__(self):
        return self.nombre

class RecepoCafetos(models.Model):
    variedad_2012 = models.ForeignKey(VariedadRecepo, related_name='recepo_2012',
        verbose_name=u'Que tipo ante de crisis',
        null=True, blank=True)
    variedad_2014 = models.ForeignKey(VariedadRecepo, related_name='recepo_2014',
        verbose_name=u'Que tipo despues de crisis',
        null=True, blank=True)

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
                            verbose_name=u'Que variedad ante de crisis',
                            null=True, blank=True)
    tipo_2014 = models.ForeignKey(TipoVariedad, related_name="tipo_2014", 
                            verbose_name=u'¿Que variedad despues de crisis',
                            null=True, blank=True)
    #mz_2012 = models.FloatField('¿Cuántas mz 2011-12?',null=True, blank=True)
    #mz_2014 = models.FloatField('¿Cuántas mz 2013-14?',null=True, blank=True)

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
                            verbose_name=u'¿Que tipo de regulacion antes ',
                            null=True, blank=True)
    tipo_2014 = models.ForeignKey(TipoSombra, related_name="tipo_2014", 
                            verbose_name=u'Que tipo de regulacion despues ',
                            null=True, blank=True)
    #mz_2012 = models.FloatField('¿Cuántas mz 2011-12?',null=True, blank=True)
    #mz_2014 = models.FloatField('¿Cuántas mz 2013-14?',null=True, blank=True)

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
                            verbose_name=u'¿Qué tipo? Antes de crisis',
                            null=True, blank=True)
    tipo_2014 = models.ForeignKey(Fertilizacion, related_name="tipo_2014", 
                            verbose_name=u'¿Qué tipo? Después de crisis ',
                            null=True, blank=True)
    mz_2012 = models.FloatField('¿Cantidad de plantas  antes de crisis?',
        null=True, blank=True)
    mz_2014 = models.FloatField('¿Cantidad de plantas  despues de crisis?',
        null=True, blank=True)

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
                            verbose_name=u'¿Qué tipo? Antes de crisis 2011-12',
                            null=True, blank=True)
    tipo_2014 = models.ForeignKey(TipoAplicacionFungicida, related_name="tipo_2014", 
                            verbose_name=u'¿Qué tipo? Después de crisis 2013-14',
                            null=True, blank=True)
    mz_2012 = models.FloatField('¿Cuántas aplicaciones? 2011-12?',
        null=True, blank=True)
    mz_2014 = models.FloatField('¿Cuántas aplicaciones?  2013-14?',
        null=True, blank=True)
    dosis_2012 = models.FloatField('¿Qué dosis? 2011-12?',
        null=True, blank=True)
    dosis_2014 = models.FloatField('¿Qué dosis?  2013-14?',
        null=True, blank=True)

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
        verbose_name_plural = '5.3 ¿Quién le orientó sobre como combatir la roya?'

    def __unicode__(self):
        pass
    
#5.4
class Productos(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Productos'

    def __unicode__(self):
        return self.nombre

CHOICE_UNIDAD = (
        (1,'ml/mz'),
        (2,'lt/mz'),
        (3,'kg/mz'),
        (4,'15. onz/pl'),
    )

class NuevosProductos(models.Model):
    producto = models.ForeignKey(Productos)
    unidad = models.IntegerField(choices=CHOICE_UNIDAD,null=True, blank=True)
    frecuencia = models.FloatField('Frecuencia de aplicación',null=True, blank=True)
    cantidad = models.FloatField('Cantidad por manzana',null=True, blank=True)

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = '5.4 ¿Que nuevos productos usan ahora para combatir la roya?'

    def __unicode__(self):
        pass

#5.5
# class AdelanteTipoCafetos(models.Model):
#     nombre = models.CharField(max_length=200)

#     class Meta:
#         verbose_name_plural = 'Tipo Cafetos'

#     def __unicode__(self):
#         return self.nombre

# class AdelantePodaCafetos(models.Model):
#     tipo_2016 = models.ForeignKey(AdelanteTipoCafetos, related_name="adelante_tipo_2016", 
#                             verbose_name=u'¿Qué tipo?  2014-16',null=True, blank=True)
#     mz_2016 = models.FloatField('¿Cuántas mz 2014-16?',null=True, blank=True)

#     encuesta = models.ForeignKey(Encuesta)

#     class Meta:
#         verbose_name_plural = '5.5-a Manejo: Poda de cafetos'

#     def __unicode__(self):
#         pass

# class AdelanteRecepoCafetos(models.Model):
#     mz_2016 = models.FloatField('¿Cuántas mz 2014-16?',null=True, blank=True)

#     encuesta = models.ForeignKey(Encuesta)

#     class Meta:
#         verbose_name_plural = '5.5-b Manejo: Recepo de cafetos'

#     def __unicode__(self):
#         pass

# class AdelanteTipoVariedad(models.Model):
#     nombre = models.CharField(max_length=200)

#     class Meta:
#         verbose_name_plural = 'Variedades de Renovación'

#     def __unicode__(self):
#         return self.nombre

# class AdelanteRenovacionCafetales(models.Model):
#     tipo_2016 = models.ForeignKey(AdelanteTipoVariedad, related_name="adelante_tipo_2016", 
#                             verbose_name=u'¿Qué tipo? 2014-16',null=True, blank=True)
#     mz_2016 = models.FloatField('¿Cuántas mz 2014-16?',null=True, blank=True)
   

#     encuesta = models.ForeignKey(Encuesta)

#     class Meta:
#         verbose_name_plural = '5.5-c Renovación de cafetales'

#     def __unicode__(self):
#         pass

# class AdelanteTipoSombra(models.Model):
#     nombre = models.CharField(max_length=200)

#     class Meta:
#         verbose_name_plural = 'Tipos de sombra'

#     def __unicode__(self):
#         return self.nombre

# class AdelanteManejoSombra(models.Model):
#     tipo_2016 = models.ForeignKey(TipoSombra, related_name="adelante_tipo_2016", 
#                             verbose_name=u'¿Qué tipo? Antes de crisis 2011-12',
#                             null=True, blank=True)
#     mz_2016 = models.FloatField('¿Cuántas mz 2011-12?',
#         null=True, blank=True)

#     encuesta = models.ForeignKey(Encuesta)

#     class Meta:
#         verbose_name_plural = '5.5-d Manejo de sombra'

#     def __unicode__(self):
#         pass

# class AdelanteFertilizacion(models.Model):
#     nombre = models.CharField(max_length=200)

#     class Meta:
#         verbose_name_plural = 'Tipos Fertilización'

#     def __unicode__(self):
#         return self.nombre

# class AdelanteManejoFertilizacion(models.Model):
#     tipo_2016 = models.ForeignKey(Fertilizacion, related_name="adelante_tipo_2016", 
#                             verbose_name=u'¿Qué tipo? 2014-16',null=True, blank=True)
#     mz_2016 = models.FloatField('¿Cantidad de plantas 2014-16?',null=True, blank=True)

#     encuesta = models.ForeignKey(Encuesta)

#     class Meta:
#         verbose_name_plural = '5.5-e Fertilización'

#     def __unicode__(self):
#         pass

# class AdelanteTipoAplicacionFungicida(models.Model):
#     nombre = models.CharField(max_length=200)

#     class Meta:
#         verbose_name_plural = 'Tipos aplicación fungicidas'

#     def __unicode__(self):
#         return self.nombre

# class AdelanteAplicacionFungicida(models.Model):
#     tipo_2016 = models.ForeignKey(TipoAplicacionFungicida, related_name="adelante_tipo_2016", 
#                             verbose_name=u'¿Qué tipo? 2014-16',
#                             null=True, blank=True)
#     mz_2016 = models.FloatField('¿Cuántas aplicaciones? 2014-16?',null=True, blank=True)
#     dosis_2016 = models.FloatField('¿Qué dosis? 2014-16?',null=True, blank=True)
    
#     encuesta = models.ForeignKey(Encuesta)

#     class Meta:
#         verbose_name_plural = '5.5-f Aplicación de fungicida'

#     def __unicode__(self):
#         pass

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
    area = models.IntegerField('Area de cafe ', choices=CHOICES_NIVEL,
        null=True, blank=True)
    variedades = models.IntegerField('Variedades de café', choices=CHOICES_VARIEDAD,
        null=True, blank=True)
    cuales = models.ManyToManyField(Variedades, related_name="cuales",
                                verbose_name=u'Cuales serán las otras variedades',
                                null=True, blank=True)
    produccion = models.IntegerField('La producción de café', choices=CHOICES_NIVEL,
        null=True, blank=True)
    igual = models.ForeignKey(Igual, verbose_name=u'Porqué igual',
        null=True, blank=True)
    mas = models.ForeignKey(Mas, verbose_name=u'Porqué más',
        null=True, blank=True)
    menos = models.ForeignKey(Menos, verbose_name=u'Porqué menos',
        null=True, blank=True)
    otros_productos = models.IntegerField('Habrá otros productos que repondrá el café o se cultivará junto al café', 
                                                                choices=CHOICES_FINCA,
                                                                null=True, blank=True)
    respuesta = models.TextField('Si la respuesta es si, cuales y porque', 
        null=True, blank=True)

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
    cuantas = models.IntegerField('2013¿Cuántas veces?',null=True, blank=True)
    profesor = models.ForeignKey(Capacitor,null=True, blank=True)
    gratis = models.IntegerField(choices=CHOICES_GRATIS,null=True, blank=True)
    metodologia = models.ManyToManyField(Metodologia, related_name="metodologia",
                                    verbose_name=u'¿Qué metodología utilizarón?',
                                    null=True, blank=True)
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
    cuantas = models.IntegerField('2013¿Cuántas veces?',null=True, blank=True)
    profesor = models.ForeignKey(Capacitor,null=True, blank=True)
    gratis = models.IntegerField(choices=CHOICES_GRATIS,null=True, blank=True)
    metodologia = models.ManyToManyField(Metodologia, 
                                        related_name="capacitacion_metodologia",
                                        verbose_name=u'¿Qué metodología utilizarón?',
                                        null=True, blank=True)
    nivel = models.IntegerField(choices=CHOICES_NIVEL_CONOCIMIENTO, 
        null=True, blank=True)

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = '5.7 Capacitaciones en tema social recibidas'

    def __unicode__(self):
        pass

#5.8
class SiLeGusta(models.Model):
    metodologia = models.ManyToManyField(Metodologia, related_name="si_metodologia",
                                verbose_name=u'¿Qué metodología de capacitación le gusto más a usted?',
                                null=True, blank=True)
    porque = models.TextField(null=True, blank=True)

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = '¿Qué metodología de capacitación le gusto más a usted?'

    def __unicode__(self):
        pass

class NoLeGusta(models.Model):
    metodologia = models.ManyToManyField(Metodologia, related_name="no_metodologia",
                                verbose_name=u' Qué metodología de capacitación le gusto menos a usted?',
                                null=True, blank=True)
    porque = models.TextField(null=True, blank=True)

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
    area = models.FloatField('Area en MZ',null=True, blank=True)
    planta = models.IntegerField('Tipo de plantas', choices=CHOICES_TIPOS_PLANTA,
        null=True, blank=True)
    edad = models.FloatField('Edad en años',null=True, blank=True)
    variedad = models.IntegerField('Variedades Predominante', 
        choices=CHOICES_VARIEDAD_PROD,
        null=True, blank=True)
    sombra = models.IntegerField('Tipo de Sombra', choices=CHOICES_TIPO_SOMBRA,
        null=True, blank=True)
    nivel = models.FloatField('Nivel de sombra%',null=True, blank=True)
    fertilizacion = models.ManyToManyField(TipoFertilizacion, related_name="fertilizante",
                                    verbose_name=u'Tipo de fertilización',
                                    null=True, blank=True)
    dosis = models.FloatField('Dosis de fertilizaciónOnza/ pl QLibras/ pl O',
        null=True, blank=True)
    fungicidas = models.ManyToManyField(TipoFungicida, related_name="fungicida",
                                        verbose_name=u'Tipo de fungicidas',
                                        null=True, blank=True)
    aplicaciones = models.FloatField('Número de aplicaciones por año',
        null=True, blank=True)
    afectadas = models.FloatField('% de plantas afectadas con Roya',
        null=True, blank=True)
    hojas = models.FloatField('% de hojas afectadas con Roya',
        null=True, blank=True)
    postula = models.FloatField('32. Número de pústula por hoja')

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = 'Detalles de incidencia de roya en algunos plantíos'

    def __unicode__(self):
        pass

class Fotos(models.Model):
    titulo = models.CharField('titulo de la foto', max_length=200)
    imagen = ImageField(upload_to=get_file_path, blank=True, null=True)

    encuesta = models.ForeignKey(Encuesta)

    fileDir = 'fotos/'

    def __unicode__(self):
            return self.titulo
    class Meta:
            verbose_name_plural = "Fotos de la finca"