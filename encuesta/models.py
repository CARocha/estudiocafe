# -*- coding: utf-8 -*-

from django.db import models
from lugar.models import Comunidad, Municipio, Departamento, Pais

# Create your models here.
class Entrevistado(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Entrevistado'
        verbose_name_plural = 'Entrevistados'

    def __unicode__(self):
        return self.nombre

class DuenoFinca(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Dueño Finca'
        verbose_name_plural = 'Dueños Fincas'

    def __unicode__(self):
        return self.nombre
    
class Organizacion(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Organizacion'
        verbose_name_plural = 'Organizaciones'

    def __unicode__(self):
        return self.nombre

class Recolector(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Recolector'

    def __unicode__(self):
        return self.nombre

CHOICE_SEXO = (
        (1, 'Hombre'),
        (2, 'Mujer'),
        (3, 'Mancomunado'),
    )

#1.1
class Encuesta(models.Model):
    fecha = models.DateField('Fecha de recolección de datos')
    recolector = models.ForeignKey(Recolector)
    nombre = models.ForeignKey(Entrevistado, verbose_name=u'Nombre de entrevistado/a')
    cedula = models.CharField(max_length=50)
    dueno = models.ForeignKey(DuenoFinca, verbose_name='Dueño de la finca')
    sexo = models.IntegerField('Sexo del dueño de la finca', choices=CHOICE_SEXO)
    finca = models.CharField('Nombre de la finca', max_length=200, 
                                null=True, blank=True)
    pais = models.ForeignKey(Pais)
    departamento = models.ForeignKey(Departamento)
    municipio = models.ForeignKey(Municipio)
    comunidad = models.ForeignKey(Comunidad)
    longitud = models.FloatField(null=True, blank=True)
    latitud = models.FloatField(null=True, blank=True)
    altitud = models.CharField(max_length=50, null=True, blank=True)
    beneficiario = models.ForeignKey(Organizacion)


    class Meta:
        verbose_name_plural = '1.1 Información general '

    def __unicode__(self):
        return self.nombre.nombre
#1.2
class SocioOrganizacion(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Organizaciones"

    def __unicode__(self):
        return self.nombre

CHOICE_DESDE = (
            (1, 'Menos de 5 años'),
            (2, 'Más de 5 años'),
            (3, 'Ninguno'),
    )

class Beneficios(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Beneficio'
        verbose_name_plural = 'Beneficios'

    def __unicode__(self):
        return self.nombre

class CreditoE(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'credito'
        verbose_name_plural = 'creditos'

    def __unicode__(self):
        return self.nombre

class DeQuien(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Organizaciones que dan credito'
        verbose_name_plural = 'Organizaciones que dan creditos'

    def __unicode__(self):
        return self.nombre
    
class QuienFinancia(models.Model):
    socio = models.ManyToManyField(SocioOrganizacion, related_name="socios")
    desde = models.IntegerField(choices=CHOICE_DESDE)
    beneficio_ser_socio = models.ManyToManyField(Beneficios, related_name="beneficiario_socio")
    tiene_credito = models.ManyToManyField(CreditoE, related_name="credito")
    de_quien = models.ManyToManyField(DeQuien, related_name="quien")

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = '1.2 Organización'

    def __unicode__(self):
        return 
    
#1.3
class ViveFamilia(models.Model):
    nombre = models.CharField(max_length=200)
    class Meta:
       
        verbose_name_plural = 'Vive Familias'

    def __unicode__(self):
        return self.nombre

CHOICE_EDUCACION = (
            (1, 'NSLE'),
            (2, 'PRIn'),
            (3, 'PRC'),
            (4, 'SECIN'),
            (5, 'Bach'),
            (6, 'Univ'),
    )

class Composicion(models.Model):
    adultos = models.IntegerField('adultos varones')
    adultas = models.IntegerField('adultas mujeres')
    jovenes_varones = models.IntegerField()
    jovenes_mujeres = models.IntegerField()
    ninos = models.IntegerField('niños')
    ninas = models.IntegerField('niñas')
    permanente_hombres = models.IntegerField()
    permanente_mujeres = models.IntegerField()
    temporales_hombres = models.IntegerField()
    temporales_mujeres = models.IntegerField()
    tecnico_hombres = models.IntegerField()
    tecnico_mujeres = models.IntegerField()
    relacion_finca_vivienda = models.ForeignKey(ViveFamilia)
    educacion_dueno = models.IntegerField('Nivel de educación de dueño de la finca?', 
                                        choices=CHOICE_EDUCACION)
    educacion_maxima_hombre = models.IntegerField('Nivel máximo de hombres de la finca?',
                                        choices=CHOICE_EDUCACION)
    educacion_maxima_mujeres = models.IntegerField('Nivel máximo de las mujeres de la finca?',
                                        choices=CHOICE_EDUCACION)

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
       
        verbose_name_plural = '1.3 Composición del grupo familiar'

    def __unicode__(self):
        return self.encuesta.nombre.nombre

#1.4
class EnergiaFinca(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'EnergiaFinca'
        verbose_name_plural = 'EnergiaFincas'

    def __unicode__(self):
        return self.nombre

class Combustible(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Combustible en la cocina'
        verbose_name_plural = 'Combustibles en la cocina'

    def __unicode__(self):
        return self.nombre

class AguaFinca(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Disponibilidad de agua en la finca'
        verbose_name_plural = 'Disponibilidad de agua en la fincas'

    def __unicode__(self):
        return self.nombre
    
class ServiciosBasicos(models.Model):
    electricidad = models.ManyToManyField(EnergiaFinca, related_name="electricidad")
    combustible = models.ManyToManyField(Combustible, related_name="combustible")
    agua_trabajo_finca = models.ManyToManyField(AguaFinca, related_name="trabaja")
    agua_consumo_humano = models.ManyToManyField(AguaFinca, related_name="consumo")

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = '1.4 Servicios básicos en la finca'

    def __unicode__(self):
        pass
    
#1.5
CHOICE_PARCELA = (
            (1, 'Propia con escritura pública'),
            (2, 'Propias con Promesa de venta'),
            (3, 'Arrendada'),
            (4, 'Propia por herencia'),
            (5, 'Propias con título de reforma agraria'),
            (6, 'Parcela en tierra comunitaria'),
            (7, 'Sin documento'),
    )
CHOICE_DOCUMENTO = (
            (1, 'Hombre'),
            (2, 'Mujer'),
            (3, 'Mancomunado'),
            (4, 'Parientes'),
            (5, 'Colectivo'),
            (6, 'No hay'),
    )

class Tenecia(models.Model):
    tipo = models.IntegerField('Tipo de tenencia de parcela', choices=CHOICE_PARCELA)
    documento = models.IntegerField('Documento legal de la parcela, a nombre de quién', 
                                                            choices=CHOICE_DOCUMENTO)

    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = '1.5 Tenencia de la tierras'

    def __unicode__(self):
        pass
    

#1.6

CHOICE_ALIMENTOS_COMPRA = (
            (1, 'Todo'),
            (2, 'Más de la Mitad'),
            (3, 'Menos de la Mitad'),
            (4, 'Nada '),
           
    )

CHOICE_SI_NO = (
            (1, 'Si'),
            (2, 'No'),
           
    )

class NecesidadAlimento(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Necesidad Alimentos'

    def __unicode__(self):
        return self.nombre
    
class Meses(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Meses del año'

    def __unicode__(self):
        return self.nombre

class TiemposCrisis(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Tiempo de crisis'

    def __unicode__(self):
        return self.nombre
    
class Seguridad(models.Model):
    compra_alimento = models.IntegerField('¿Qué parte de alimentos básicos que consume la familia o la en la finca se compra?',
                                                                            choices=CHOICE_ALIMENTOS_COMPRA)
    cubrir_necesidades = models.IntegerField('¿Siente que en algunos años no ha podido cubrir las necesidades básicas de alimentación de la familia o la finca? ',
                                            choices=CHOICE_SI_NO)
    porque_no_cubre = models.ManyToManyField(NecesidadAlimento,related_name="cubre",
        verbose_name=u'¿Porque motivo no se ha podido cubrir las necesidades de alimentos de la familia o la finca?')
    meses_dificiles = models.ManyToManyField(Meses, related_name="dificiles",
        verbose_name=u'¿Cuáles son los meses más difíciles para la alimentación de la familia o la finca?')
    soluciones_crisis = models.ManyToManyField(TiemposCrisis, related_name="crisis",
                    verbose_name=u'¿Qué soluciones y practicas implementa en los tiempos de crisis o escasez de alimentos?')
    
    encuesta = models.ForeignKey(Encuesta)

    class Meta:
       
        verbose_name_plural = '1.6 Seguridad alimentaria de la familia'

    def __unicode__(self):
        pass
