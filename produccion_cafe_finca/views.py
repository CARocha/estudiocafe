# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from encuesta.models import Encuesta, CHOICE_ALIMENTOS_COMPRA, NecesidadAlimento, Meses, TiemposCrisis, Seguridad
from .models import *
from django.db.models import Avg, Sum, Max, Min
import collections
from encuesta.views import _query_set_filtrado
from vulnerabilidades_finca.models import TipoClima, TipoYear, ElClima, SueloFertilidad, \
CHOICES_TEXTURA, CHOICES_PROFUNDIDAD,CHOICES_PRESENCIA,CHOICES_PENDIENTE,CHOICES_DRENAJE, \
CHOICES_PREPARAN,CHOICES_OBRA_CONSERVACION,CHOICES_SUELO_FERTIL,CHOICES_CAFETALES_DEGRADADOS, \
CHOICES_FERTILIZACION, Opciones,Respuestas,OtroRiesgos,CHOICES_MONITOREO,CHOICES_MONITOREO_PLAGAS, \
CHOICES_MONITOREO_REGISTRO, CHOICES_FALTA_RECURSOS, CHOICES_CERTIFICACION, CHOICES_RECONOCIDA_MONITOREADA, \
CHOICES_INFRAESTRUCTURA,FaltaRecurso,TiposCertificados,ElaboraPlanes,Mitigacion



#3.7
def salida131(request, template='encuesta/salida_c/corte.html'):
    encuestas = _query_set_filtrado(request)
    conteo = encuestas.count()
    
    corte = {}
    for obj in CHOICES_CORTE:
        valor = Beneficiado.objects.filter(encuesta__in=encuestas, cortes=obj[0]).count()
        corte[obj[1]] = valor

    separan = {}
    for obj in CHOICES_SI_NO_BENEFICIARIO:
        valor = Beneficiado.objects.filter(encuesta__in=encuestas, separan=obj[0]).count()
        separan[obj[1]] = valor

    despulpan = {}
    for obj in CHOICES_DESPULPAN_FERMENTAN:
        valor = Beneficiado.objects.filter(encuesta__in=encuestas, despulpan_fermentan=obj[0]).count()
        despulpan[obj[1]] = valor

    estado = {}
    for obj in CHOICES_ESTADO_HUMEDO:
        valor = Beneficiado.objects.filter(encuesta__in=encuestas, estado=obj[0]).count()
        estado[obj[1]] = valor

    calibra = {}
    for obj in CHOICES_CALIBRAN:
        valor = Beneficiado.objects.filter(encuesta__in=encuestas, calibran=obj[0]).count()
        calibra[obj[1]] = valor

    revisa = {}
    for obj in CHOICES_CALIBRAN:
        valor = Beneficiado.objects.filter(encuesta__in=encuestas, revisan=obj[0]).count()
        revisa[obj[1]] = valor


    return render(request, template, locals())

#3.7
def salida132(request, template='encuesta/salida_c/cortes.html'):
    encuestas = _query_set_filtrado(request)
    conteo = encuestas.count()
    
   
    agua_despulpar = {}
    for obj in CHOICES_DESPULPAR:
        valor = Beneficiado.objects.filter(encuesta__in=encuestas, despulpar=obj[0]).count()
        agua_despulpar[obj[1]] = valor

    fermenta = {}
    for obj in CHOICES_FERMENTAN:
        valor = Beneficiado.objects.filter(encuesta__in=encuestas, fermentan=obj[0]).count()
        fermenta[obj[1]] = valor

    orea = {}
    for obj in CHOICES_OREAN:
        valor = Beneficiado.objects.filter(encuesta__in=encuestas, orean=obj[0]).count()
        orea[obj[1]] = valor

    beneficiado = {}
    for obj in BeneficioSeco.objects.all():
        valor = Beneficiado.objects.filter(encuesta__in=encuestas, beneficiado_seco=obj).count()
        beneficiado[obj.nombre] = valor

    calidad = {}
    for obj in CHOICE_SI_NO:
        valor = Beneficiado.objects.filter(encuesta__in=encuestas, calidad=obj[0]).count()
        calidad[obj[1]] = valor

    calidad_cafe = {}
    for obj in CalidadCafe.objects.all():
        valor = Beneficiado.objects.filter(encuesta__in=encuestas, determina_calidad=obj).count()
        calidad_cafe[obj.nombre] = valor


    return render(request, template, locals())

#1.6
def salida17(request, template='encuesta/salida_g/seguridad.html'):
    encuestas = _query_set_filtrado(request)
    conteo = encuestas.count()

    alimentos = {}
    for obj in CHOICE_ALIMENTOS_COMPRA:
        valor = Seguridad.objects.filter(encuesta__in=encuestas, compra_alimento=obj[0]).count()
        alimentos[obj[1]] = valor

    necesidad_basica = {}
    for obj in CHOICE_SI_NO:
        valor = Seguridad.objects.filter(encuesta__in=encuestas, cubrir_necesidades=obj[0]).count()
        necesidad_basica[obj[1]] = valor

    motivos_cubre_necesidad = {}
    for obj in NecesidadAlimento.objects.all():
        valor = Seguridad.objects.filter(encuesta__in=encuestas, porque_no_cubre=obj).count()
        motivos_cubre_necesidad[obj.nombre] = valor

    meses_sin_alimento = {}
    for obj in Meses.objects.all():
        valor = Seguridad.objects.filter(encuesta__in=encuestas, meses_dificiles=obj).count()
        meses_sin_alimento[obj.nombre] = valor

    mitigar_falta_alimento = {}
    for obj in TiemposCrisis.objects.all():
        valor = Seguridad.objects.filter(encuesta__in=encuestas, soluciones_crisis=obj).count()
        mitigar_falta_alimento[obj.nombre] = valor

    return render(request, template, locals())

#Clima 4.1
def salida18(request, template='encuesta/salida_g/elclima.html'):
    encuestas = _query_set_filtrado(request)
    conteo = encuestas.count()

    clima_opciones = {}
    for obj in TipoClima.objects.all():
        valor = ElClima.objects.filter(encuesta__in=encuestas, clima=obj).count()
        clima_opciones[obj.nombre] = valor

    clima_fechas = {}
    for x in TipoYear.objects.all():
        clima_fechas[x.nombre] = {}
        for obj in TipoClima.objects.all():
            valor = ElClima.objects.filter(encuesta__in=encuestas, clima=obj, fecha=x).count()
            clima_fechas[x.nombre][obj.nombre] = (valor)
    

    return render(request, template, locals())

#Clima 4.2
def salida19(request, template='encuesta/salida_g/elsuelo.html'):
    encuestas = _query_set_filtrado(request)
    conteo = encuestas.count()
   
    textura = {}
    for obj in CHOICES_TEXTURA:
        valor = SueloFertilidad.objects.filter(encuesta__in=encuestas, textura=obj[0]).count()
        textura[obj[1]] = valor

    profundidad = {}
    for obj in CHOICES_PROFUNDIDAD:
        valor = SueloFertilidad.objects.filter(encuesta__in=encuestas, profundidad=obj[0]).count()
        profundidad[obj[1]] = valor

    presencia = {}
    abundancia = {}
    materia = {}
    for obj in CHOICES_PRESENCIA:
        valor = SueloFertilidad.objects.filter(encuesta__in=encuestas, presencia=obj[0]).count()
        valor1 = SueloFertilidad.objects.filter(encuesta__in=encuestas, abundancia=obj[0]).count()
        valor2 = SueloFertilidad.objects.filter(encuesta__in=encuestas, materia_organica=obj[0]).count()
        presencia[obj[1]] = valor
        abundancia[obj[1]] = valor1
        materia[obj[1]] = valor2

    pendiente = {}
    for obj in CHOICES_PENDIENTE:
        valor = SueloFertilidad.objects.filter(encuesta__in=encuestas, pendiente=obj[0]).count()
        pendiente[obj[1]] = valor

    drenaje = {}
    for obj in CHOICES_DRENAJE:
        valor = SueloFertilidad.objects.filter(encuesta__in=encuestas, drenaje=obj[0]).count()
        drenaje[obj[1]] = valor

    preparan = {}
    for obj in CHOICES_PREPARAN:
        valor = SueloFertilidad.objects.filter(encuesta__in=encuestas, preparan=obj[0]).count()
        preparan[obj[1]] = valor
        
    fertilidad = {}
    foliar = {}
    conservacion = {}
    for obj in CHOICE_SI_NO:
        valor = SueloFertilidad.objects.filter(encuesta__in=encuestas, foliar=obj[0]).count()
        valor1 = SueloFertilidad.objects.filter(encuesta__in=encuestas, conservacion=obj[0]).count()
        valor2 = SueloFertilidad.objects.filter(encuesta__in=encuestas, fertilidad=obj[0]).count()
        foliar[obj[1]] = valor
        conservacion[obj[1]] = valor1
        fertilidad[obj[1]] = valor2

    fertilizacion = {}
    for obj in CHOICES_FERTILIZACION:
        valor = SueloFertilidad.objects.filter(encuesta__in=encuestas, fertilizacion=obj[0]).count()
        fertilizacion[obj[1]] = valor
        

    obra = {}
    for obj in CHOICES_OBRA_CONSERVACION:
        valor = SueloFertilidad.objects.filter(encuesta__in=encuestas, obra_conservacion=obj[0]).count()
        obra[obj[1]] = valor

    fertil = {}
    for obj in CHOICES_SUELO_FERTIL:
        valor = SueloFertilidad.objects.filter(encuesta__in=encuestas, fertil=obj[0]).count()
        fertil[obj[1]] = valor

    degrados = {}
    for obj in CHOICES_CAFETALES_DEGRADADOS:
        valor = SueloFertilidad.objects.filter(encuesta__in=encuestas, degrados=obj[0]).count()
        degrados[obj[1]] = valor

    return render(request, template, locals())

#Clima 4.4
def salida20(request, template='encuesta/salida_g/otrosriesgos.html'):
    encuestas = _query_set_filtrado(request)
    conteo = encuestas.count()
    #Opciones,Respuestas,OtroRiesgos
    otros ={}
    for obj in Opciones.objects.all():
        otros[obj.nombre] = {}
        for m in Respuestas.objects.all():
            valor = OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=obj, respuesta=m).count()
            otros[obj.nombre] [m.nombre]= (valor)

    return render(request, template, locals())

#Clima 4.5
def salida21(request, template='encuesta/salida_g/mitigacion.html'):
    encuestas = _query_set_filtrado(request)
    conteo = encuestas.count()

    plagas = {}
    recursos = {}
    almacenamiento = {}
    formaorganica = {}
    contrato = {}
    certificado = {}
    planmanejo = {}
    plannegocio = {}
    planinversion = {}
    for obj in CHOICE_SI_NO:
        valor = Mitigacion.objects.filter(encuesta__in=encuestas, monitoreo_plagas=obj[0]).count()
        valor1 = Mitigacion.objects.filter(encuesta__in=encuestas, recursos=obj[0]).count()
        valor2 = Mitigacion.objects.filter(encuesta__in=encuestas, almacenamiento=obj[0]).count()
        valor3 = Mitigacion.objects.filter(encuesta__in=encuestas, forma_organizada=obj[0]).count()
        valor4 = Mitigacion.objects.filter(encuesta__in=encuestas, contrato=obj[0]).count()
        valor5 = Mitigacion.objects.filter(encuesta__in=encuestas, certificado=obj[0]).count()
        valor6 = Mitigacion.objects.filter(encuesta__in=encuestas, plan_manejo=obj[0]).count()
        valor7 = Mitigacion.objects.filter(encuesta__in=encuestas, plan_negocio=obj[0]).count()
        valor8 = Mitigacion.objects.filter(encuesta__in=encuestas, plan_inversion=obj[0]).count()
        plagas[obj[1]] = valor
        recursos[obj[1]] = valor1
        almacenamiento[obj[1]] = valor2
        formaorganica[obj[1]] = valor3
        contrato[obj[1]] = valor4
        certificado[obj[1]] = valor5
        planmanejo[obj[1]] = valor6
        plannegocio[obj[1]] = valor7
        planinversion[obj[1]] = valor8

    frecuencia = {}
    for obj in CHOICES_MONITOREO:
        valor = Mitigacion.objects.filter(encuesta__in=encuestas, cada_cuanto=obj[0]).count()
        frecuencia[obj[1]] = valor

    como_realiza = {}
    for obj in CHOICES_MONITOREO_PLAGAS:
        valor = Mitigacion.objects.filter(encuesta__in=encuestas, como_realiza=obj[0]).count()
        como_realiza[obj[1]] = valor

    registro_monitoreo = {}
    for obj in CHOICES_MONITOREO_REGISTRO:
        valor = Mitigacion.objects.filter(encuesta__in=encuestas, falta_recurso=obj[0]).count()
        registro_monitoreo[obj[1]] = valor

    faltarecurso = {}
    for obj in FaltaRecurso.objects.all():
        valor = Mitigacion.objects.filter(encuesta__in=encuestas, registro_monitoreo=obj).count()
        faltarecurso[obj.nombre] = valor

    tipocertificado = {}
    for obj in TiposCertificados.objects.all():
        valor = Mitigacion.objects.filter(encuesta__in=encuestas, tipos_certificados=obj).count()
        tipocertificado[obj.nombre] = valor

    reconocido = {}
    for obj in CHOICES_RECONOCIDA_MONITOREADA:
        valor = Mitigacion.objects.filter(encuesta__in=encuestas, reconocida=obj[0]).count()
        reconocido[obj[1]] = valor

    infraestructura = {}
    for obj in CHOICES_INFRAESTRUCTURA:
        valor = Mitigacion.objects.filter(encuesta__in=encuestas, infraestructura=obj[0]).count()
        infraestructura[obj[1]] = valor

    elaboraplanes = {}
    for obj in ElaboraPlanes.objects.all():
        valor = Mitigacion.objects.filter(encuesta__in=encuestas, elabora=obj).count()
        elaboraplanes[obj.nombre] = valor

    return render(request, template, locals())
   
def _get_view(request, vista):
    if vista in VALID_VIEWS:
        return VALID_VIEWS[vista](request)
    else:
        raise ViewDoesNotExist("Tried %s in module %s Error: View not define in VALID_VIEWS." % (vista, 'encuesta.views'))

VALID_VIEWS = {
    'beneficiados': salida131,
    'beneficiado': salida132,
    'seguridad': salida17,
    'elclima': salida18,
    'elsuelo': salida19,
    'otros': salida20,
    'mitigar': salida21,
    }
