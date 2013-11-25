# -*- coding: utf-8 -*-

from django.db import models
from encuesta.models import Encuesta, CHOICE_SI_NO

#4. Vulnerabilidades de la finca
#4.1
class TipoClima(models.Model):
    nombre = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Tipo Clima'
        verbose_name_plural = 'Tipo Climas'

    def __unicode__(self):
        return self.nombre
    
class TipoYear(models.Model):
    nombre = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Tipo Clima'
        verbose_name_plural = 'Tipo Climas'

    def __unicode__(self):
        return self.nombre

class ElClima(models.Model):
    clima = models.ForeignKey(TipoClima)
    fecha = models.ManyToManyField(TipoYear, related_name="fecha",null=True, blank=True)

    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name = '4.1 El Clima'
        verbose_name_plural = '4.1 El Clima'

    def __unicode__(self):
        pass
    
#4.2
CHOICES_TEXTURA = (
            (1, 'Arcilloso'),
            (2, 'Limoso'),
            (3, 'Arenoso'),
            (4, 'Francoarenoso'),
            (5, 'Francolimoso'),
    )
CHOICES_PROFUNDIDAD = (
            (1, 'Muy profunda'),
            (2, 'Media profunda'),
            (3, 'Poca profunda'),
    )
CHOICES_PRESENCIA = (
            (1, 'Alta'),
            (2, 'Media'),
            (3, 'Baja'),
    )

CHOICES_PENDIENTE = (
            (1, 'Plana'),
            (2, 'Inclinada'),
            (3, 'Muy inclinada'),
    )

CHOICES_DRENAJE = (
            (1, 'Bueno'),
            (2, 'Regular'),
            (3, 'Malo'),
    )

CHOICES_PREPARAN = (
            (1, 'Quema'),
            (2, 'Trabaja en crudo'),
            (3, 'Uso de herbicidas'),
            (4, 'Usa cobertura'),
    )
CHOICES_FERTILIZACION = (
            (1, 'Química'),
            (2, 'Orgánica'),
            (3, 'ambos'),
            (4, 'Ninguna'),
    )
CHOICES_OBRA_CONSERVACION = (
            (1, 'Barrera viva'),
            (2, 'Barrera muerta'),
            (3, 'Terraza'),
            (4, 'Acequia'),
            (5, 'Curvas a nivel'),
    )
CHOICES_SUELO_FERTIL = (
            (1, 'Si es fértil'),
            (2, 'en parte es fértil'),
            (3, 'No es fértil'),
        
    )
CHOICES_CAFETALES_DEGRADADOS = (
            (1, 'Si esta degradado'),
            (2, 'en parte esta degradado'),
            (3, 'No esta degradado'),
        
    )

class SueloFertilidad(models.Model):
    textura = models.IntegerField('¿Cuál es el tipo de textura del suelo?', 
        choices=CHOICES_TEXTURA,
        null=True, blank=True)
    profundidad = models.IntegerField('¿Cuál es la profundidad de suelo?', 
        choices=CHOICES_PROFUNDIDAD,
        null=True, blank=True)
    presencia = models.IntegerField('¿Cómo es la presencia de lombrices en el suelo?', 
                                                        choices=CHOICES_PRESENCIA,
                                                        null=True, blank=True)
    abundancia = models.IntegerField('¿Cómo es la abundancia de los raíces en los primeros 6 pulgadas de suelo?', 
                                                        choices=CHOICES_PRESENCIA,
                                                        null=True, blank=True)
    pendiente = models.IntegerField('¿Cuál es el pendiente del terreno?', 
        choices=CHOICES_PENDIENTE,
        null=True, blank=True)
    drenaje = models.IntegerField('¿Cómo es el drenaje del suelo?', 
        choices=CHOICES_DRENAJE,
        null=True, blank=True)
    materia_organica = models.IntegerField('¿Cómo es el contenido de materia orgánica?', 
        choices=CHOICES_PRESENCIA,
        null=True, blank=True)
    preparan = models.IntegerField('¿Cómo preparan el terreno para la siembra?', 
        choices=CHOICES_PREPARAN,
        null=True, blank=True)
    fertilidad = models.IntegerField('¿Realiza análisis de fertilidad de suelos?', 
        choices=CHOICE_SI_NO,
        null=True, blank=True)
    foliar = models.IntegerField('¿Realiza análisis de foliar?', 
        choices=CHOICE_SI_NO,
        null=True, blank=True)
    fertilizacion = models.IntegerField('¿Qué tipo de fertilización realiza?', 
        choices=CHOICES_FERTILIZACION,
        null=True, blank=True)
    conservacion = models.IntegerField('¿Realiza práctica de conservación de suelo?', 
        choices=CHOICE_SI_NO,
        null=True, blank=True)
    obra_conservacion = models.IntegerField('¿Qué tipo de obra para conservación de suelo REALIZA?', 
                                                        choices=CHOICES_OBRA_CONSERVACION,
                                                        null=True, blank=True)
    fertil = models.IntegerField('¿Considera el suelo de los cafetales fértil?', 
                                                        choices=CHOICES_SUELO_FERTIL,
                                                        null=True, blank=True)
    degrados = models.IntegerField('¿Considera el suelo de los cafetales degrados y sin vida?', 
                                                        choices=CHOICES_CAFETALES_DEGRADADOS,
                                                        null=True, blank=True)

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name = '4.2 El suelo y fertilidad'
        verbose_name_plural = '4.2 El suelo y fertilidad'

    def __unicode__(self):
        pass

#4.3
CHOICES_ANIOS_PLAGA = (
            (1, '2011-12'),
            (2, '2012-13'),
            (3, '2013-14'),       
    )
class Plagas(models.Model):
    nombre = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Plagas'
        verbose_name_plural = 'Plagass'

    def __unicode__(self):
        return self.nombre
    
class LasPlagas(models.Model):
    fecha = models.IntegerField('Años',null=True, blank=True)
    gallo = models.ManyToManyField(Plagas, related_name="gallo", 
        verbose_name=u'Ojo de gallo',null=True, blank=True)
    roya = models.ManyToManyField(Plagas, related_name="roya", 
        verbose_name=u'La Roya',null=True, blank=True)
    hierro = models.ManyToManyField(Plagas, related_name="hierro", 
        verbose_name=u'Mancha de hierro',null=True, blank=True)
    antracnosis = models.ManyToManyField(Plagas, related_name="antracnosis", 
        verbose_name=u'Antracnosis',null=True, blank=True)
    broca = models.ManyToManyField(Plagas, related_name="broca", verbose_name=u'Broca del fruto')
    nematodos = models.ManyToManyField(Plagas, related_name="nematodos", verbose_name=u'Nematodos')

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name = '4.3. Las plagas'
        verbose_name_plural = '4.3. Las plagas'

    def __unicode__(self):
        pass

#4.4
class Causa(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = "Causa"
        
class Opciones(models.Model):
    causa = models.ForeignKey(Causa)
    nombre = models.CharField(max_length=100)
    
    def __unicode__(self):
        return '%s - %s' % (self.causa.nombre, self.nombre)
        
    class Meta:
        verbose_name_plural = "Opciones"
        
class Respuestas(models.Model):
    nombre = models.CharField(max_length=100)
   
    def __unicode__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = "Respuestas"
        
class OtroRiesgos(models.Model):
    motivo = models.ForeignKey(Opciones)
    respuesta = models.ManyToManyField(Respuestas, null=True, blank=True)

    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "4.4 Otros riesgos"

#4.5
CHOICES_MONITOREO = (
            (1, 'Mensual'),
            (2, 'Cada 3 meses'),
            (3, 'Cada 6 meses'), 
            (4, 'Anual'),      
    )
CHOICES_MONITOREO_PLAGAS = (
            (1, 'Observaciones'),
            (2, 'Recuentos'),
    )
CHOICES_MONITOREO_REGISTRO = (
            (1, 'Si'),
            (2, 'No'),
            (3, 'Si y Procesa y usa los datos'),
    )

CHOICES_FALTA_RECURSOS = (
            (1, 'Insumos'),
            (2, 'Pago de Mano de obra'),
            (3, 'Gastos operativos'), 
            (4, 'Inversiones'),      
    )
CHOICES_CERTIFICACION = (
            (1, 'CJ'),
            (2, 'ORG'),
            (3, 'RFA'), 
            (4, 'UTZ'),
            (5, 'CP'),
    )
CHOICES_RECONOCIDA_MONITOREADA= (
            (1, 'Si'),
            (2, 'No'),
            (3, 'Puntaje SCAA'),
    )
CHOICES_INFRAESTRUCTURA= (
            (1, 'Si Buena calidad'),
            (2, 'Si mala Calidad'),
            (3, 'No'),
    )
CHOICES_ELABORAR_PLANES = (
            (1, 'Propio'),
            (2, 'Contrate AT'),
            (3, 'ONG'), 
            (4, 'Empresas'),
            (5, 'Cooperativa'),
            (6, 'Asociación'),
            (7, 'Banco o Micro-finanza'),
    )

class Mitigacion(models.Model):
    monitoreo_plagas = models.IntegerField('¿Realiza monitoreo de plagas y enfermedades?', 
                                                                choices=CHOICE_SI_NO)
    cada_cuanto = models.IntegerField('¿Cada cuanto realiza monitoreo de plagas y enfermedades?', 
                                                                choices=CHOICES_MONITOREO)
    como_realiza = models.IntegerField('¿Cómo realiza monitoreo de plagas y enfermedades?', 
                                                                choices=CHOICES_MONITOREO_PLAGAS)
    registro_monitoreo = models.IntegerField('¿Si lleva registro de  monitoreo de plagas y enfermedades?', 
                                                                choices=CHOICES_MONITOREO_REGISTRO)
    recursos = models.IntegerField('¿Cuenta con suficiente recursos para manejo de finca?', 
                                                                choices=CHOICE_SI_NO)
    falta_recursos = models.IntegerField('¿Para que cosas hace falta los recursos?', 
                                                                choices=CHOICES_FALTA_RECURSOS)
    almacenamiento = models.IntegerField('¿Cuenta con obras para almacenamiento de agua?', 
                                                                choices=CHOICE_SI_NO)
    forma_organizada = models.IntegerField('¿Vende su Café en forma organizada a través de una asociación o cooperativa o grupo o Empresa?', 
                                                                choices=CHOICE_SI_NO)
    contrato = models.IntegerField('¿Cuenta con un contrato para la venta de café?', choices=CHOICE_SI_NO)
    certificado = models.IntegerField('¿Esta certificado los cafetales?', choices=CHOICE_SI_NO)
    tipo_certificado = models.IntegerField('¿Qué tipo de certificación?', choices=CHOICES_CERTIFICACION)
    reconocida = models.IntegerField('¿La calidad de su café en reconocida y monitoreada?', 
                                                                choices=CHOICES_RECONOCIDA_MONITOREADA)
    infraestructura = models.IntegerField('¿Dispone infraestructura para beneficio húmedo  y almacenamiento de cosecha?', 
                                                                choices=CHOICES_INFRAESTRUCTURA)
    plan_manejo = models.IntegerField('¿Cuenta con plan de manejo de la finca?', choices=CHOICE_SI_NO)
    plan_negocio = models.IntegerField('¿Cuenta con un plan de negocio para el cultivo de café?', 
                                                                choices=CHOICE_SI_NO)
    plan_inversion = models.IntegerField('¿Cuenta con un plan de inversión para el cultivo de café?',
                                                                choices=CHOICE_SI_NO)
    elaborar = models.IntegerField('¿Quién apoyo para elaborar estos planes?', 
                                                                choices=CHOICES_ELABORAR_PLANES)

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name = '4.5 Mitigación de los riesgos '
        verbose_name_plural = '4.5 Mitigación de los riesgos '

    def __unicode__(self):
        pass
    