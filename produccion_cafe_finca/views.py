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
    global_si = 0
    for obj in CHOICE_SI_NO:
        valor = Seguridad.objects.filter(encuesta__in=encuestas, cubrir_necesidades=obj[0]).count()
        global_si = Seguridad.objects.filter(encuesta__in=encuestas, cubrir_necesidades=1).count()
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
    total_sistema = Encuesta.objects.all().count()

    clima_opciones = collections.OrderedDict()
    suma_opciones = 0
    cantidad_items = 0
    for obj in TipoClima.objects.all():
        valor = ElClima.objects.filter(encuesta__in=encuestas, clima=obj).count()
        suma_opciones += valor
        cantidad_items += 1
        clima_opciones[obj.nombre] = valor

    valor_divisor = round((total_sistema * 5),4)
    valor_relativo = round(float(suma_opciones) / float(valor_divisor),4)

    clima_fechas = collections.OrderedDict()
    for obj in TipoClima.objects.all():
        clima_fechas[obj.nombre] = collections.OrderedDict()
        for x in TipoYear.objects.all():
            valor = ElClima.objects.filter(encuesta__in=encuestas, clima=obj, fecha=x).count()
            clima_fechas[obj.nombre][x.nombre] = (valor)
    

    return render(request, template, locals())

# 4.2
def salida19(request, template='encuesta/salida_g/elsuelo.html'):
    encuestas = _query_set_filtrado(request)
    conteo = encuestas.count()
   
    #textura 
    arcilloso = SueloFertilidad.objects.filter(encuesta__in=encuestas,textura=1).count()
    limoso = SueloFertilidad.objects.filter(encuesta__in=encuestas,textura=2).count()
    arenoso = SueloFertilidad.objects.filter(encuesta__in=encuestas,textura=3).count()
    francoarenoso = SueloFertilidad.objects.filter(encuesta__in=encuestas,textura=4).count()
    francolimoso = SueloFertilidad.objects.filter(encuesta__in=encuestas,textura=5).count()
    total_textura = round(float((arcilloso*5) + (arenoso*4) + (limoso*2)) / float(conteo),4) 
    

    #profundidad = {}
    muy_profunda = SueloFertilidad.objects.filter(encuesta__in=encuestas, profundidad=1).count()
    media_profunda = SueloFertilidad.objects.filter(encuesta__in=encuestas, profundidad=2).count()
    poca_profunda = SueloFertilidad.objects.filter(encuesta__in=encuestas, profundidad=3).count()
    total_profundidad = round(float((muy_profunda*0) + (media_profunda*3) + (poca_profunda*5)) / float(conteo),4) 
    

    #presencia lombrices
    lombrice_alta =SueloFertilidad.objects.filter(encuesta__in=encuestas, presencia=1).count()
    lombrice_media =SueloFertilidad.objects.filter(encuesta__in=encuestas, presencia=2).count()
    lombrice_baja =SueloFertilidad.objects.filter(encuesta__in=encuestas, presencia=3).count()
    total_lombrice = round(float((lombrice_alta*0) + (lombrice_media*3) + (lombrice_baja*5)) / float(conteo),4) 
    
    #abundancia
    abundancia_alta =SueloFertilidad.objects.filter(encuesta__in=encuestas, abundancia=1).count()
    abundancia_media =SueloFertilidad.objects.filter(encuesta__in=encuestas, abundancia=2).count()
    abundancia_baja =SueloFertilidad.objects.filter(encuesta__in=encuestas, abundancia=3).count()
    total_abundancia = round(float((abundancia_alta*5) + (abundancia_media*3) + (abundancia_baja*0)) / float(conteo),4) 

    #materia
    materia_alta =SueloFertilidad.objects.filter(encuesta__in=encuestas, materia_organica=1).count()
    materia_media =SueloFertilidad.objects.filter(encuesta__in=encuestas, materia_organica=2).count()
    materia_baja =SueloFertilidad.objects.filter(encuesta__in=encuestas, materia_organica=3).count()
    total_materia = round(float((materia_alta*0) + (materia_media*3) + (materia_baja*5)) / float(conteo),4) 

    #pendiente = {}
    plana = SueloFertilidad.objects.filter(encuesta__in=encuestas, pendiente=1).count()
    inclinada = SueloFertilidad.objects.filter(encuesta__in=encuestas, pendiente=2).count()
    muy_inclinada =SueloFertilidad.objects.filter(encuesta__in=encuestas, pendiente=3).count()
    total_pendiente = round(float((plana*0) + (inclinada*3) + (muy_inclinada*5)) / float(conteo),4) 

    #drenaje = {}
    bueno = SueloFertilidad.objects.filter(encuesta__in=encuestas, drenaje=1).count()
    regular =SueloFertilidad.objects.filter(encuesta__in=encuestas, drenaje=2).count()
    malo =SueloFertilidad.objects.filter(encuesta__in=encuestas, drenaje=3).count()
    total_drenaje = round(float((bueno*0) + (regular*3) + (malo*5)) / float(conteo),4) 

    #preparan = {}
    quema = SueloFertilidad.objects.filter(encuesta__in=encuestas, preparan=1).count()
    trabaja_en_crudo = SueloFertilidad.objects.filter(encuesta__in=encuestas, preparan=2).count()
    uso_de_herbicidas = SueloFertilidad.objects.filter(encuesta__in=encuestas, preparan=3).count()
    usa_cobertura =SueloFertilidad.objects.filter(encuesta__in=encuestas, preparan=4).count()
    total_preparan = round(float((quema*5) + (trabaja_en_crudo*3) + (uso_de_herbicidas*5) + (usa_cobertura*0)) / float(conteo),4) 

    #fertilidad = {}
    fertilidad_si =SueloFertilidad.objects.filter(encuesta__in=encuestas, fertilidad=1).count()
    fertilidad_no = SueloFertilidad.objects.filter(encuesta__in=encuestas, fertilidad=2).count()
    total_fertilidad = round(float((fertilidad_si*0) + (fertilidad_no*5)) / float(conteo),4) 

    #foliar = {}
    foliar_si =SueloFertilidad.objects.filter(encuesta__in=encuestas, foliar=1).count()
    foliar_no =SueloFertilidad.objects.filter(encuesta__in=encuestas, foliar=2).count()
    total_foliar = round(float((foliar_si*0) + (foliar_no*5)) / float(conteo),4) 

    #conservacion = {}
    conservacion_si =SueloFertilidad.objects.filter(encuesta__in=encuestas, conservacion=1).count()
    conservacion_no =SueloFertilidad.objects.filter(encuesta__in=encuestas, conservacion=2).count()
    total_conservacion = round(float((conservacion_si*0) + (conservacion_no*5)) / float(conteo),4) 

    #fertilizacion = {}
    quimica =SueloFertilidad.objects.filter(encuesta__in=encuestas, fertilizacion=1).count()
    organica =SueloFertilidad.objects.filter(encuesta__in=encuestas, fertilizacion=2).count()
    ambos =SueloFertilidad.objects.filter(encuesta__in=encuestas, fertilizacion=3).count()
    ninguna =SueloFertilidad.objects.filter(encuesta__in=encuestas, fertilizacion=4).count()
    total_fertilizacion = round(float((quimica*5) + (ambos*3) + (ninguna*5)) / float(conteo),4) 

    #obra = {}
    barrera_viva =SueloFertilidad.objects.filter(encuesta__in=encuestas, obra_conservacion=1).count()
    barrera_muerta =SueloFertilidad.objects.filter(encuesta__in=encuestas, obra_conservacion=2).count()
    terraza =SueloFertilidad.objects.filter(encuesta__in=encuestas, obra_conservacion=3).count()
    acequia =SueloFertilidad.objects.filter(encuesta__in=encuestas, obra_conservacion=4).count()
    curvas_a_nivel = SueloFertilidad.objects.filter(encuesta__in=encuestas, obra_conservacion=5).count()
    #total_obra = round(((barrera_viva*0) + (barrera_muerta*0) + (terraza*0)) / conteo,4) 

    #fertil = {}
    si_es_fertil =SueloFertilidad.objects.filter(encuesta__in=encuestas, fertil=1).count()
    en_parte_fertil =SueloFertilidad.objects.filter(encuesta__in=encuestas, fertil=2).count()
    no_es_fertil =SueloFertilidad.objects.filter(encuesta__in=encuestas, fertil=3).count()
    total_fertil = round(float((si_es_fertil*0) + (en_parte_fertil*3) + (no_es_fertil*5)) / float(conteo),4) 

    #degrados = {}
    si_esta_degradado=SueloFertilidad.objects.filter(encuesta__in=encuestas, degrados=1).count()
    en_parte_esta_degradado=SueloFertilidad.objects.filter(encuesta__in=encuestas, degrados=2).count()
    no_esta_degradado = SueloFertilidad.objects.filter(encuesta__in=encuestas, degrados=3).count()
    total_degrados = round(float((si_esta_degradado*5) + (en_parte_esta_degradado*3) + (no_esta_degradado*0)) / float(conteo),4) 

    total_riesgos = round(float(total_textura+total_profundidad+total_lombrice+\
        total_abundancia+total_materia+total_pendiente+total_drenaje+\
        total_preparan+total_fertilidad+total_foliar+total_conservacion+\
        total_fertilizacion+total_fertil+total_degrados) / float(14),4)

    return render(request, template, locals())

# 4.4
def salida20(request, template='encuesta/salida_g/otrosriesgos.html'):
    encuestas = _query_set_filtrado(request)
    conteo = encuestas.count()
    #Opciones,Respuestas,OtroRiesgos
    otros ={}
    for obj in Opciones.objects.all():
        otros[obj] = {}
        for m in Respuestas.objects.all():
            valor = OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=obj, respuesta=m).count()
            otros[obj] [m.nombre]= (valor)


    #Asperctos agricolas - las variedades
    no_adecuadas = OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=1, respuesta=5).count()
    si_adecuadas = OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=1, respuesta=4).count()
    total_variedad = no_adecuadas * 5
    #hay falta de semilla
    semilla_siempre =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=2, respuesta=1).count()
    semilla_veces =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=2, respuesta=2).count()
    semilla_nunca =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=2, respuesta=3).count()
    total_semilla = (semilla_siempre * 5) + (semilla_veces * 3)
    #mala calidad de semilla
    calidad_semilla_siempre =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=3, respuesta=1).count()
    calidad_semilla_veces =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=3, respuesta=2).count()
    calidad_semilla_nunca =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=3, respuesta=3).count()
    total_calidad = (calidad_semilla_siempre * 5) + (calidad_semilla_veces * 3)
    #manejo de cultivos no adecuados
    cultivos_siempre =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=4, respuesta=1).count()
    cultivos_veces =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=4, respuesta=2).count()
    cultivos_nunca =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=4, respuesta=3).count()
    total_cultivos = (cultivos_siempre * 5) + (cultivos_veces * 3)
    #fertiliazacion no adecuado
    fertilizacion_siempre =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=5, respuesta=1).count()
    fertilizacion_veces =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=5, respuesta=2).count()
    fertilizacion_nunca =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=5, respuesta=3).count()
    total_fertilizacion = (fertilizacion_siempre * 5) + (fertilizacion_veces * 3)
    #mucho danio de plaga
    plaga_siempre =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=6, respuesta=1).count()
    plaga_veces =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=6, respuesta=2).count()
    plaga_nunca =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=6, respuesta=3).count()
    total_plaga = (plaga_siempre * 5) + (plaga_veces * 3)
    total_agricola = round(float(total_variedad + total_semilla + total_calidad + total_cultivos + total_fertilizacion +total_plaga) / float(conteo * 6),4)
    
    #Riesgos productivos
    #baja produccion de cafe
    bajaproduccion_siempre =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=7, respuesta=1).count()
    bajaproduccion_veces =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=7, respuesta=2).count()
    bajaproduccion_nunca =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=7, respuesta=3).count()
    total_bajaproduccion = (bajaproduccion_siempre * 5) + (bajaproduccion_veces * 3)
    #poca floracion
    floracion_siempre =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=8, respuesta=1).count()
    floracion_veces =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=8, respuesta=2).count()
    floracion_nunca =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=8, respuesta=3).count()
    total_floracion = (floracion_siempre * 5) + (floracion_veces * 3)
    #mucho aborto
    aborto_siempre =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=9, respuesta=1).count()
    aborto_veces =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=9, respuesta=2).count()
    aborto_nunca =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=9, respuesta=3).count()
    total_aborto = (aborto_siempre * 5) + (aborto_veces * 3)
    #mucha caida de frutos
    frutos_siempre =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=10, respuesta=1).count()
    frutos_veces =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=10, respuesta=2).count()
    frutos_nunca =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=10, respuesta=3).count()
    total_frutos = (frutos_siempre * 5) + (frutos_veces * 3)
    #marcada bianualidad
    marcada_siempre =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=11, respuesta=1).count()
    marcada_veces =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=11, respuesta=2).count()
    marcada_nunca =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=11, respuesta=3).count()
    total_marcada = (marcada_siempre * 5) + (marcada_veces * 3)
    #mala recoleccion de frutos
    recolecion_siempre =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=12, respuesta=1).count()
    recolecion_veces =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=12, respuesta=2).count()
    recolecion_nunca =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=12, respuesta=3).count()
    total_recolecion = (recolecion_siempre * 5) + (recolecion_veces * 3)
    #falta de mano de obra para el corte
    mo_siempre =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=13, respuesta=1).count()
    mo_veces =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=13, respuesta=2).count()
    mo_nunca =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=13, respuesta=3).count()
    total_mo = (mo_siempre * 5) + (mo_veces * 3)
    #beneficiado humedo no adecuado
    humedo_siempre =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=14, respuesta=1).count()
    humedo_veces =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=14, respuesta=2).count()
    humedo_nunca =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=14, respuesta=3).count()
    total_humedo = (humedo_siempre * 5) + (humedo_veces * 3)
    total_productivo = round(float(total_bajaproduccion+total_floracion+total_aborto+total_frutos+total_marcada+total_recolecion+total_mo+total_humedo)/float(conteo*8),4)

    #Riesgos de mercado
    #bajo precio de cafe
    precio_siempre =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=15, respuesta=1).count()
    precio_veces =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=15, respuesta=2).count()
    precio_nunca =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=15, respuesta=3).count()
    total_precio = (precio_siempre * 5) + (precio_veces * 3)
    #falta de venta
    venta_siempre =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=16, respuesta=1).count()
    venta_veces =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=16, respuesta=2).count()
    venta_nunca =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=16, respuesta=3).count()
    total_venta = (venta_siempre * 5) + (venta_veces * 3)
    #Estafa de contrato
    estafa_siempre =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=17, respuesta=1).count()
    estafa_veces =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=17, respuesta=2).count()
    estafa_nunca =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=17, respuesta=3).count()
    total_estafa = (estafa_siempre * 5) + (estafa_veces * 3)
    #mala calidad cafe
    mala_siempre =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=18, respuesta=1).count()
    mala_veces =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=18, respuesta=2).count()
    mala_nunca =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=18, respuesta=3).count()
    total_mala = (mala_siempre * 5) + (mala_veces * 3)
    #pagos atrasado
    pagos_siempre =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=19, respuesta=1).count()
    pagos_veces =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=19, respuesta=2).count()
    pagos_nunca =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=19, respuesta=3).count()
    total_pagos = (pagos_siempre * 5) + (pagos_veces * 3)
    #problema de traslado de cosecha
    traslado_siempre =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=20, respuesta=1).count()
    traslado_veces =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=20, respuesta=2).count()
    traslado_nunca =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=20, respuesta=3).count()
    total_traslado = (traslado_siempre * 5) + (traslado_veces * 3)
    total_mercado = round(float(total_precio+total_venta+total_estafa+total_mala+total_pagos+total_traslado)/float(conteo*6),4)

    #riesgos finaciamiento
    #disponibilidad credito a corto plazo
    corto_siempre =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=21, respuesta=1).count()
    corto_veces =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=21, respuesta=2).count()
    corto_nunca =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=21, respuesta=3).count()
    total_corto = (corto_siempre * 5) + (corto_veces * 3)
    #credito a mediano plazo
    mediano_siempre =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=22, respuesta=1).count()
    mediano_veces =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=22, respuesta=2).count()
    mediano_nunca =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=22, respuesta=3).count()
    total_mediano = (mediano_siempre * 5) + (mediano_veces * 3)
    #credito a largo plazo
    largo_siempre =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=23, respuesta=1).count()
    largo_veces =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=23, respuesta=2).count()
    largo_nunca =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=23, respuesta=3).count()
    total_largo = (largo_siempre * 5) + (largo_veces * 3)
    #altos intereses
    intereses_siempre =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=24, respuesta=1).count()
    intereses_veces =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=24, respuesta=2).count()
    intereses_nunca =OtroRiesgos.objects.filter(encuesta__in=encuestas, motivo=24, respuesta=3).count()
    total_intereses = (intereses_siempre * 5) + (intereses_veces * 3)
    total_financiero = round(float(total_corto+total_mediano+total_largo+total_intereses)/float(conteo*4),4)
    

    return render(request, template, locals())

# 4.5
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
        valor = Mitigacion.objects.filter(encuesta__in=encuestas, falta_recurso=obj).count()
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
