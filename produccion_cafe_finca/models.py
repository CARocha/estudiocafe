# -*- coding: utf-8 -*-

from django.db import models
from encuesta.models import Encuesta, CHOICE_SI_NO, Meses

#3. Sistema de producción café en la finca
#3.1 Área de café

class EstadoActual(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'EstadoActual'
        verbose_name_plural = 'EstadoActuals'

    def __unicode__(self):
        return self.nombre
    
class AreaCafe(models.Model):
    estado = models.ForeignKey(EstadoActual)
    once = models.FloatField('2010-2011')
    doce = models.FloatField('2011-12')
    trece = models.FloatField('2012-13')
    catorse = models.FloatField('2013-14')

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name = '3.1 Área de café'
        verbose_name_plural = '3.1 Área de café'

    def __unicode__(self):
        pass
 
 #3.2

class Plantio(models.Model):
    nombre = models.CharField(max_length=100) 

    class Meta:
        verbose_name = 'Plantio'
        verbose_name_plural = 'Plantios'

    def __unicode__(self):
        return self.nombre   

class Variedades(models.Model):
    nombre = models.CharField(max_length=100) 

    class Meta:
        verbose_name = 'Variedad'
        verbose_name_plural = 'Variedades'

    def __unicode__(self):
        return self.nombre

class VariedadEdadRoya(models.Model):
    nombre_plantio = models.ForeignKey(Plantio)
    area = models.FloatField('Area Mz')
    variedades = models.ManyToManyField(Variedades, related_name="variedades")
    produccion_2012 = models.FloatField('Producción 2011-12 qq perg/mz')
    produccion_2013 = models.FloatField('Producción 2012-13 qq perg/mz')
    produccion_2014 = models.FloatField('Estiamdo produccion 2013-14 qq perg/mz')
    nivel_roya = models.FloatField('Nivel de roya 2013-14 basado en la impresión plantas afectadas')

    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = '3.2 Variedad, edad, roya y producción'

    def __unicode__(self):
        pass

#3.3
class ResistenteRoya(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Resistente Roya'
        verbose_name_plural = 'Resistente Royas'

    def __unicode__(self):
        return self.nombre

class Semilla(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Semillas'

    def __unicode__(self):
        return self.nombre

class DecideSembrar(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Decide Sembrar'

    def __unicode__(self):
        return self.nombre

class Criterios(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Criterios'

    def __unicode__(self):
        return self.nombre


class ProduccionVivero(models.Model):
    vivero_finca = models.IntegerField('¿Actualmente tiene vivero de café en la finca?',
                                                                choices=CHOICE_SI_NO)
    plantas_vivero = models.FloatField('¿Cuántas plantas hay en el vivero?')
    plantas_finca = models.FloatField('¿Cuántas plantas para sembrar en la finca?')
    plantas_vender = models.FloatField('¿Cuántas plantas para vender en la finca?')
    plantas_injertadas = models.FloatField('¿Cuántas plantas son injertadas?')
    edad_planta = models.FloatField('¿Cuál es la edad de las plantas de vivero? en meses')
    variedad = models.ManyToManyField(Variedades, related_name="variedad", 
                                      verbose_name=u'¿Qué  variedades hay en el vivero?')
    resistente_roya = models.ManyToManyField(ResistenteRoya, related_name="resistente", 
                                                    verbose_name=u'¿Cuáles son resistentes a roya? ¿Cuántas de ellas tienen? ')
    consigue_semilla = models.ManyToManyField(Semilla, related_name="semilla",
                                            verbose_name=u'¿Actualmente EN DONDE consiguen las semillas o plantas?')
    disponible = models.ManyToManyField(Variedades, related_name="disponible",
                                            verbose_name=u'¿Qué variedades están disponibles para la siembra en estos lugares?')
    costo_planta_caturra = models.FloatField('Seleccion CATURRA')
    costo_planta_catimore = models.FloatField('Lineas de CATIMORES')
    costo_planta_hibridas = models.FloatField('Hibridas')
    pagar_caturra = models.FloatField()
    pagar_catimore = models.FloatField()
    pagar_hibrida = models.FloatField()
    decide = models.ManyToManyField(DecideSembrar, related_name="decide" ,
                                    verbose_name=u'¿Cómo decide sobre que variedad a sembrar?')
    criterio = models.ManyToManyField(Criterios, related_name="criterio",
                        verbose_name=u'¿Qué criterio es más importante para usted cuando usted selecciona una variedad?')           

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
       verbose_name = '3.3 La  producción de vivero y su disponibilidad a los productores'
       verbose_name_plural = '3.3 La  producción de vivero y su disponibilidad a los productores'

    def __unicode__(self):
       pass

#3.4
CHOICES_ANIOS = (
            (1, '2011-12'),
            (2, '2012-13'),
            (3, '2013-14'),
    )

class Manejos(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Manejos'
        verbose_name_plural = 'Manejoss'

    def __unicode__(self):
        return self.nombre

class ManejoCafetales(models.Model):
    fecha = models.IntegerField('Años', choices=CHOICES_ANIOS)
    manejo_cafeto = models.ManyToManyField(Manejos, related_name="cafeto",
                                        verbose_name=u'Manejo de tejido o poda de cafetos')
    manejo_sombra = models.ManyToManyField(Manejos, related_name="sombra",
                                        verbose_name=u'Manejo o poda de sombra')
    fertilizante_suelo = models.ManyToManyField(Manejos, related_name="suelo",
                                                verbose_name=u'Aplicación de fertilizantes en el suelo')
    fertilizante_foliares = models.ManyToManyField(Manejos, related_name="foliares",
                                                    verbose_name=u'Aplicación de  fertilizantes foliares')
    fungicidas = models.ManyToManyField(Manejos, related_name="fungicida",
                                        verbose_name=u'Aplicación de Fungicidas')
    insecticidas = models.ManyToManyField(Manejos, related_name="insecticida",
                                        verbose_name=u'Aplicaciones de insecticidas')
    nematicidas = models.ManyToManyField(Manejos, related_name="nematicidas",
                                        verbose_name=u'Aplicaciones de nematicidas')

    encuesta = models.ForeignKey(Encuesta)


    class Meta:
        verbose_name = '3.4 Manejo de los cafetales'
        verbose_name_plural = '3.4 Manejo de los cafetales'

    def __unicode__(self):
        pass

CHOICES_ANIOS_otro = (
            (4, 'Mes que realizan'),
    )

class MesesManejoCafe(models.Model):
    fecha = models.IntegerField('Años', choices=CHOICES_ANIOS_otro)
    mes_manejo_cafeto = models.ManyToManyField(Meses, related_name="manejo_cefeto",
                                            verbose_name=u'Manejo de tejido o poda de cafetos')
    mes_manejo_sombra = models.ManyToManyField(Meses, related_name="manejo_sombra", 
                                            verbose_name=u'Manejo o poda de sombra')
    mes_fertilizante_suelo = models.ManyToManyField(Meses, related_name="fertilizante_suelo",
                                                    verbose_name=u'Aplicación de fertilizantes en el suelo')
    mes_fertilizante_foliares = models.ManyToManyField(Meses, related_name="fertilizante_foliares",
                                                verbose_name=u'Aplicación de  fertilizantes foliares')
    mes_fungicidas = models.ManyToManyField(Meses, related_name="mes_fungicidas",
                                            verbose_name=u'Aplicación de Fungicidas')
    mes_insecticidas = models.ManyToManyField(Meses, related_name="mes_insecticida",
                                            verbose_name=u'Aplicaciones de insecticidas')
    mes_nematicidas = models.ManyToManyField(Meses, related_name="mes_nematicidas",
                                            verbose_name=u'Aplicaciones de nematicidas')
    encuesta = models.ForeignKey(Encuesta)


    class Meta:
        verbose_name = '3.4-2 Meses Manejo de los cafetales'
        verbose_name_plural = '3.4-2 Meses Manejo de los cafetales'

    def __unicode__(self):
        pass

#3.5
class TiposInsumos(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Tipos Insumo'
        verbose_name_plural = 'Tipos Insumos'

    def __unicode__(self):
        return self.nombre

class NombreTipos(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Nombre Tipos'
        verbose_name_plural = 'Nombre Tipos'

    def __unicode__(self):
        return self.nombre

class UsoInsumos(models.Model):
    tipo = models.ForeignKey(TiposInsumos)
    nombre = models.ForeignKey(NombreTipos)
    aplicaciones = models.FloatField('Número de aplicaciones')
    cantidad = models.FloatField('Cantidad por mz Lts, Lb, Kg')
    momento = models.ManyToManyField(Meses, related_name="momento",
                                    verbose_name=u'Momento de aplicación')

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name = '3.5 Uso de insumos (2013-14)'
        verbose_name_plural = '3.5 Uso de insumos (2013-14)'

    def __unicode__(self):
        pass
    
#3.6
class Opciones(models.Model):
    nombre = models.CharField(max_length=200)
    class Meta:
        verbose_name = 'Opciones'
        verbose_name_plural = 'Opcioness'

    def __unicode__(self):
        return self.nombre

CHOICES_NIVEL = (
            (1, 'No utiliza'),
            (2, 'En pequeño escala'),
            (3, 'En mayor escala'),
            (4, 'En toda la finca'),
    )

class UsoOpcionesAgroecologica(models.Model):
    opcion = models.ForeignKey(Opciones)
    nivel = models.IntegerField('Nivel de uso en la finca', choices=CHOICES_NIVEL)

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name = '3.6 Uso de opciones agroecológicos en los cafetale'
        verbose_name_plural = '3.6 Uso de opciones agroecológicos en los cafetale'

    def __unicode__(self):
        pass
    
#3.7
CHOICES_CORTE = (
            (1, 'Cortan Solo rojito'),
            (2, 'Cortan Rojito y pinto'),
            (3, 'Cortan parejo'),
    )
CHOICES_SI_NO_BENEFICIARIO = (
            (1, 'Si'),
            (2, 'No'),
            (3, 'No siempre'),
    )
CHOICES_DESPULPAN_FERMENTAN = (
            (1, 'En la finca'),
            (2, 'Finca vecina'),
            (3, 'Cooperativa/asociación'),
    )
CHOICES_ESTADO_HUMEDO = (
            (1, 'Bueno'),
            (2, 'Regular'),
            (3, 'Malo'),
    )
CHOICES_CALIBRAN = (
            (1, 'Al inicio de la cosecha'),
            (2, 'Varias veces durante el corte'),
            (3, 'Nunca'),
    )
CHOICES_DESPULPAR = (
            (1, 'Quebrada'),
            (2, 'Agua de pozo'),
            (3, 'Agua de montaña'),
            (4, 'Agua potable'),
    )
CHOICES_FERMENTAN = (
            (1, 'Saco'),
            (2, 'Cajón de madera'),
            (3, 'Pilas de concreto'),
            (4, 'Pilas con cerámica'),
    )
CHOICES_OREAN = (
            (1, 'Patio'),
            (2, 'Patio sobre plástico'),
            (3, 'Zarandas'),
            (4, 'Túneles'),
    )
class BeneficioSeco(models.Model):
    nombre = models.CharField(max_length=200)
    class Meta:
        verbose_name = 'Beneficio Seco'
        verbose_name_plural = 'Beneficio Secos'

    def __unicode__(self):
        return self.nombre

class CalidadCafe(models.Model):
    nombre = models.CharField(max_length=200)
    class Meta:
        verbose_name = 'Calidad Cafe '
        verbose_name_plural = 'Calidad Cafe'

    def __unicode__(self):
        return self.nombre

class Beneficiado(models.Model):
    cortes = models.IntegerField('¿Cómo realizaron los cortes?', 
                        choices=CHOICES_CORTE)
    separan = models.IntegerField('¿Separan sobre maduros y granos negros?',
                         choices=CHOICES_SI_NO_BENEFICIARIO)
    despulpan_fermentan = models.IntegerField('¿Dónde despulpan y fermentan el café?', 
                        choices=CHOICES_DESPULPAN_FERMENTAN)
    estado = models.IntegerField('¿Cómo es el estado de su beneficio húmedo?', 
                        choices=CHOICES_ESTADO_HUMEDO)
    calibran = models.IntegerField('¿Cada cuanto calibran la maquina para despulpar café?', 
                        choices=CHOICES_CALIBRAN)
    revisan = models.IntegerField('¿Cada cuánto revisan la camisa y pechero?', 
                        choices=CHOICES_CALIBRAN)
    despulpar = models.IntegerField('¿ De dónde saca el agua para despulpar y lavar?', 
                        choices=CHOICES_DESPULPAR)
    fermentan = models.IntegerField('¿Dónde fermentan el café?', choices=CHOICES_FERMENTAN)
    orean = models.IntegerField('¿Dónde orean el café?', choices=CHOICES_OREAN)
    beneficiado_seco = models.ForeignKey(BeneficioSeco, 
                            verbose_name=u'¿ Donde se realizan el beneficiado seco?')
    calidad = models.IntegerField('¿Conoce la calidad de la taza de su café?', 
                                choices=CHOICE_SI_NO)
    determina_calidad = models.ForeignKey(CalidadCafe, 
                            verbose_name=u'¿Quién determino la calidad de la taza de su café')
    precio = models.IntegerField('¿Reciben un sobre precio para su café?', 
                                choices=CHOICE_SI_NO)
    cuanto = models.FloatField('¿Cuánto por qq oro?')

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name = '3.7 Beneficiado'
        verbose_name_plural = '3.7 Beneficiado'

    def __unicode__(self):
        pass
        
#3.7 la comercializacion
CHOICES_ANIOS_comercializacion = (
            (1, '2011-12'),
            (2, '2012-13'),
            (3, '2013-14'),       
    )

class Comercializacion(models.Model):
    fecha = models.IntegerField('Años', choices=CHOICES_ANIOS_comercializacion)
    p_total = models.FloatField('Producción total de café qq pergamino')
    i_venta_cafe = models.FloatField('Intermediarios: Venta de café qq pergamino')
    i_precio = models.FloatField('Intermediarios: Precio pagado en C$ por qq pergamino')
    c_venta = models.FloatField('Cooperativa o Assoc: Venta de café qq pergamino')
    c_precio = models.FloatField('Cooperativa o Assoc: Precio pagado en C$ por qq pergamino')
    e_venta = models.FloatField('Empresa exportadora: Venta a las empresas acopiadoras')
    e_precio = models.FloatField('Empresa exportadora: Precio en C$ por qq pergamino')

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name = '3.7 La comercialización'
        verbose_name_plural = '3.7 La comercialización'

    def __unicode__(self):
        pass

#3.8  
CHOICES_ANIOS_CREDITO = (
            (1, '2010-11'),
            (2, '2011-12'),
            (3, '2012-13'), 
            (3, '2013-14'),      
    )

CHOICES_ANIOS_FACILIDAD = (
            (1, 'F'),
            (2, 'R'),
            (3, 'D'), 
    )

class Credito(models.Model):
    fecha = models.IntegerField('Años', choices=CHOICES_ANIOS_CREDITO)
    monto = models.FloatField('Monto de crédito corto plazo')
    cobertura = models.FloatField('% de cobertura de la necesidad')
    credito_mediano = models.FloatField('Monto de crédito de mediano plazo')
    necesidad = models.FloatField('% cobertura de la necesidad')
    credito_largo = models.FloatField('Monto de crédito de largo plazo')
    cobertura_necesidad = models.FloatField('% cobertura de la necesidad')
    facilidad = models.IntegerField('Facilidad de pago', choices=CHOICES_ANIOS_FACILIDAD)

    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name = '3.8 Crédito para producción de café'
        verbose_name_plural = '3.8 Crédito para producción de café'

    def __unicode__(self):
        pass
    
