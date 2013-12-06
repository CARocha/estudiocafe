# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from encuesta.models import Encuesta
from .models import *
from django.db.models import Avg, Sum, Max, Min
import collections
from encuesta.views import _query_set_filtrado


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


def _get_view(request, vista):
    if vista in VALID_VIEWS:
        return VALID_VIEWS[vista](request)
    else:
        raise ViewDoesNotExist("Tried %s in module %s Error: View not define in VALID_VIEWS." % (vista, 'encuesta.views'))

VALID_VIEWS = {
    'beneficiados': salida131,
    'beneficiado': salida132,
    }
