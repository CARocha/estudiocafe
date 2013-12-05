# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from encuesta.models import Encuesta
from .models import *
from django.db.models import Avg, Sum, Max, Min
import collections
from encuesta.views import _query_set_filtrado
from vulnerabilidades_finca.models import  Plagas, LasPlagas
from produccion_cafe_finca.models import AreaCafe

def salida17(request, template='encuesta/salida_e/enfermedades.html'):
    encuestas = _query_set_filtrado(request)
    conteo = encuestas.count()
    total = Encuesta.objects.all().count()

    ojo_gallo = collections.OrderedDict()
    for obj in Plagas.objects.all():
        valor = LasPlagas.objects.filter(encuesta__in=encuestas, gallo=obj).count()
        ojo_gallo[obj.nombre] = valor

    la_roya = collections.OrderedDict()
    for obj in Plagas.objects.all():
        valor = LasPlagas.objects.filter(encuesta__in=encuestas, roya=obj).count()
        la_roya[obj.nombre] = valor

    mancha = collections.OrderedDict()
    for obj in Plagas.objects.all():
        valor = LasPlagas.objects.filter(encuesta__in=encuestas, hierro=obj).count()
        mancha[obj.nombre] = valor

    antracnosi = collections.OrderedDict()
    for obj in Plagas.objects.all():
        valor = LasPlagas.objects.filter(encuesta__in=encuestas, antracnosis=obj).count()
        antracnosi[obj.nombre] = valor

    fruto = collections.OrderedDict()
    for obj in Plagas.objects.all():
        valor = LasPlagas.objects.filter(encuesta__in=encuestas, broca=obj).count()
        fruto[obj.nombre] = valor

    nematodo = collections.OrderedDict()
    for obj in Plagas.objects.all():
        valor = LasPlagas.objects.filter(encuesta__in=encuestas, nematodos=obj).count()
        nematodo[obj.nombre] = valor


    return render(request, template, locals())

def salida171(request, template='encuesta/salida_e/roya.html'):
    encuestas = _query_set_filtrado(request)
    conteo = encuestas.count()
    total = Encuesta.objects.all().count()

    area_total_doce = AreaCafe.objects.filter(encuesta__in=encuestas, estado__id=1).aggregate(doce=Sum('doce'))['doce']
    area_total_trece = AreaCafe.objects.filter(encuesta__in=encuestas, estado__id=1).aggregate(trece=Sum('trece'))['trece']
    area_total_catorce = AreaCafe.objects.filter(encuesta__in=encuestas, estado__id=1).aggregate(catorse=Sum('catorse'))['catorse']
    
    roya = collections.OrderedDict()
    for obj in Impactos.objects.all():
        doce = ImpactoRoya.objects.filter(encuesta__in=encuestas, impacto=obj).aggregate(doce=Sum('doce'))['doce']
        trece = ImpactoRoya.objects.filter(encuesta__in=encuestas, impacto=obj).aggregate(trece=Sum('trece'))['trece']
        catorce = ImpactoRoya.objects.filter(encuesta__in=encuestas, impacto=obj).aggregate(catorce=Sum('catorce'))['catorce']
        roya[obj.nombre] = (doce,trece,catorce)

    return render(request, template, locals())

def salida172(request, template='encuesta/salida_e/poda.html'):
    encuestas = _query_set_filtrado(request)
    conteo = encuestas.count()
    
    poda = collections.OrderedDict()
    for obj in TipoCafetos.objects.all():
        antes = PodaCafetos.objects.filter(encuesta__in=encuestas, tipo_2012=obj).count()
        despues = PodaCafetos.objects.filter(encuesta__in=encuestas, tipo_2014=obj).count()
        
        poda[obj.nombre] = (antes,despues)

    return render(request, template, locals())

def salida173(request, template='encuesta/salida_e/recepo.html'):
    encuestas = _query_set_filtrado(request)
    conteo = encuestas.count()
    
    recepo = collections.OrderedDict()
    for obj in VariedadRecepo.objects.all():
        antes = RecepoCafetos.objects.filter(encuesta__in=encuestas, variedad_2012=obj).count()
        despues = RecepoCafetos.objects.filter(encuesta__in=encuestas, variedad_2014=obj).count()
        
        recepo[obj.nombre] = (antes,despues)

    return render(request, template, locals())

def salida174(request, template='encuesta/salida_e/variedades.html'):
    encuestas = _query_set_filtrado(request)
    conteo = encuestas.count()
    
    variedad = collections.OrderedDict()
    for obj in TipoVariedad.objects.all():
        antes = RenovacionCafetales.objects.filter(encuesta__in=encuestas, tipo_2012=obj).count()
        despues = RenovacionCafetales.objects.filter(encuesta__in=encuestas, tipo_2014=obj).count()
        
        variedad[obj.nombre] = (antes,despues)

    return render(request, template, locals())

def salida175(request, template='encuesta/salida_e/sombra.html'):
    encuestas = _query_set_filtrado(request)
    conteo = encuestas.count()
    
    sombra = collections.OrderedDict()
    for obj in TipoSombra.objects.all():
        antes = ManejoSombra.objects.filter(encuesta__in=encuestas, tipo_2012=obj).count()
        despues = ManejoSombra.objects.filter(encuesta__in=encuestas, tipo_2014=obj).count()
        
        sombra[obj.nombre] = (antes,despues)

    return render(request, template, locals())

def salida176(request, template='encuesta/salida_e/fertilizacion.html'):
    encuestas = _query_set_filtrado(request)
    conteo = encuestas.count()
    
    fertilizacion = collections.OrderedDict()
    for obj in Fertilizacion.objects.all():
        antes = ManejoFertilizacion.objects.filter(encuesta__in=encuestas, tipo_2012=obj).count()
        despues = ManejoFertilizacion.objects.filter(encuesta__in=encuestas, tipo_2014=obj).count()
        
        fertilizacion[obj.nombre] = (antes,despues)

    min_antes = ManejoFertilizacion.objects.filter(encuesta__in=encuestas).aggregate(min_antes=Min('mz_2012'))['min_antes']
    min_despues = ManejoFertilizacion.objects.filter(encuesta__in=encuestas).aggregate(min_despues=Min('mz_2014'))['min_despues']

    max_antes = ManejoFertilizacion.objects.filter(encuesta__in=encuestas).aggregate(max_antes=Min('mz_2012'))['max_antes']
    max_despues = ManejoFertilizacion.objects.filter(encuesta__in=encuestas).aggregate(max_despues=Min('mz_2014'))['max_despues']

    return render(request, template, locals())

def salida177(request, template='encuesta/salida_e/fungicidas.html'):
    encuestas = _query_set_filtrado(request)
    conteo = encuestas.count()
    
    fungicidas = collections.OrderedDict()
    for obj in TipoAplicacionFungicida.objects.all():
        antes = AplicacionFungicida.objects.filter(encuesta__in=encuestas, tipo_2012=obj).count()
        despues = AplicacionFungicida.objects.filter(encuesta__in=encuestas, tipo_2014=obj).count()
        
        fungicidas[obj.nombre] = (antes,despues)

    min_antes = AplicacionFungicida.objects.filter(encuesta__in=encuestas).aggregate(min_antes=Min('mz_2012'))['min_antes']
    min_despues = AplicacionFungicida.objects.filter(encuesta__in=encuestas).aggregate(min_despues=Min('mz_2014'))['min_despues']

    max_antes = AplicacionFungicida.objects.filter(encuesta__in=encuestas).aggregate(max_antes=Min('mz_2012'))['max_antes']
    max_despues = AplicacionFungicida.objects.filter(encuesta__in=encuestas).aggregate(max_despues=Min('mz_2014'))['max_despues']

    return render(request, template, locals())

def _get_view(request, vista):
    if vista in VALID_VIEWS:
        return VALID_VIEWS[vista](request)
    else:
        raise ViewDoesNotExist("Tried %s in module %s Error: View not define in VALID_VIEWS." % (vista, 'encuesta.views'))

VALID_VIEWS = {
    'incidencia-enfermedades': salida17,
    'impacto-roya': salida171,
    'cambio-poda': salida172,
    'cambio-recepo': salida173,
    'cambio-variedad': salida174,
    'manejo-sombra': salida175,
    'fertilizacion': salida176,
    'fungicidas': salida177,
    }
