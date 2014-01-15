# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from .forms import ConsultarForm
import json
from lugar.models import Departamento, Comunidad
from django.db.models import Avg, Sum, Max, Min, Count
from vulnerabilidades_finca.models import *
from produccion_finca.models import *
from produccion_cafe_finca.models import *

import collections


def index(request):
    familias = Encuesta.objects.all().count()

    return render(request, 'index.html', locals())

def _query_set_filtrado(request):
    params = {}
    if request.session['departamento']:
        if not request.session['municipio']:
            municipios = Municipio.objects.filter(departamento__in=request.session['departamento'])
            params['municipio__in'] = municipios
        else:
            #if request.session['comunidad']:
            #   params['comunidad__in'] = request.session['comunidad']
            if request.session['municipio']:
                params['municipio__in'] = request.session['municipio']

    if request.session['empresa']:
        params['beneficiarios__in'] = request.session['empresa']
    
    if request.session['altitud']:
        altitud = int(request.session['altitud'])
        if altitud == 1:
            params['altitud__range'] = (400,800)
        elif altitud == 2:
            params['altitud__range'] = (801,1200)
        else:
            params['altitud__gt'] = 1201
        
    if request.session['area_finca']:
        params['usotierra__tierra__id'] = 1
        area_finca = int(request.session['area_finca'])
        if area_finca == 1:
            params['usotierra__area__range'] = (1, 10)
        elif area_finca == 2:
            params['usotierra__area__range'] = (11, 50)
        else:
            params['usotierra__area__gt'] = 50

    if request.session['area_cafe']:
        params['usotierra__tierra__id'] = 8
        area_cafe = int(request.session['area_cafe'])
        if area_cafe == 1:
            params['usotierra__area__range'] = (1, 10)
        elif area_cafe == 2:
            params['usotierra__area__range'] = (11, 50)
        else:
            params['usotierra__area__gt'] = 50

    if request.session['nivel_educacion']:
        params['composicion__educacion_dueno'] = request.session['nivel_educacion']

    if request.session['variedad_predominate']:
        params['produccionvivero__variedad_predomindante__in'] = request.session['variedad_predominate']


    if request.session['variedad_viviero']:
        params['produccionvivero__variedad__in'] = request.session['variedad_viviero']

    if request.session['reduccion_cosecha']:
        params['impactoroya__impacto__id'] = 5
        catorce = int(request.session['reduccion_cosecha'])
        if catorce == 1:
            params['impactoroya__catorce__range'] = (0, 10)
        elif catorce == 2:
            params['impactoroya__catorce__range'] = (11, 30)
        else:
            params['impactoroya__catorce__gt'] = 31

    if request.session['credito']:
        params['quienfinancia__tiene_credito'] = request.session['credito']

    encuestas = Encuesta.objects.filter( ** params)

    return encuestas

def consultar(request, template="encuesta/consultar.html"):
    if request.method == 'POST':
        form = ConsultarForm(request.POST)
        if form.is_valid():
            #request.session['anio'] = form.cleaned_data['anio']
            request.session['departamento'] = form.cleaned_data['departamento']
            request.session['municipio'] = form.cleaned_data['municipio']
            #request.session['comunidad'] = form.cleaned_data['comunidad']            
            request.session['altitud'] = form.cleaned_data['altitud']
            request.session['empresa'] = form.cleaned_data['empresa']
            request.session['area_finca'] = form.cleaned_data['area_finca']
            request.session['area_cafe'] = form.cleaned_data['area_cafe']
            request.session['nivel_educacion'] = form.cleaned_data['nivel_educacion']
            request.session['variedad_predominate'] = form.cleaned_data['variedad_predominate']
            request.session['variedad_viviero'] = form.cleaned_data['variedad_viviero']
            request.session['reduccion_cosecha'] = form.cleaned_data['reduccion_cosecha']
            request.session['credito'] = form.cleaned_data['credito']

            request.session['centinel'] = 1
            encuestas = _query_set_filtrado(request).count()
        
            if encuestas != 0:
                return HttpResponseRedirect('/indicadores/')
            else:
                nono = 2
    else:
        form = ConsultarForm()       
    return render(request, template, locals())

def indicadores(request, template='encuesta/indicadores.html'):
    encuestas = _query_set_filtrado(request).count()
    return render(request,template, locals())

def salida1(request, template='encuesta/salida_a/informacion.html'):
    encuestas = _query_set_filtrado(request)
    conteo = encuestas.count()
    total = Encuesta.objects.all().count()

    mujer = encuestas.filter(sexo=2).count()
    hombre = encuestas.filter(sexo=1).count()
    mancumudado = encuestas.filter(sexo=3).count()

    educacion = {}
    for obj in CHOICE_EDUCACION:
        valor = Composicion.objects.filter(encuesta__in=encuestas, educacion_dueno=obj[0]).count()
        educacion[obj[1]] = valor

    tenencia = {}
    for obj in CHOICE_PARCELA:
        valor = Tenecia.objects.filter(encuesta__in=encuestas, tipo=obj[0]).count()
        tenencia[obj[1]] = valor

    documento = {}
    for obj in CHOICE_DOCUMENTO:
        valor = Tenecia.objects.filter(encuesta__in=encuestas, documento=obj[0]).count()
        documento[obj[1]] = valor

    return render(request, template, locals())

def salida2(request, template='encuesta/salida_a/ubicacion.html'):
    encuestas = _query_set_filtrado(request)
    conteo = encuestas.count()
    total = Encuesta.objects.all().count()

    departamento = {}
    for obj in Departamento.objects.all():
        valor = encuestas.filter(departamento=obj).count()
        departamento[obj.nombre] = valor

    municipio = {}
    for obj in Municipio.objects.all():
        valor = encuestas.filter(municipio=obj).count()
        municipio[obj.nombre] = valor

    CHOICE_ALTITUD = (
            ((400,800), '400-800'),
            ((801,1200), '801-1200'),
            ((1201,100000), 'Más de 1201'),
    )

    altitud = {}
    for obj in CHOICE_ALTITUD:
        valor = encuestas.filter(altitud__range=obj[0]).count()
        altitud[obj[1]] = valor

    return render(request, template, locals())

def salida3(request, template='encuesta/salida_a/servicios.html'):
    encuestas = _query_set_filtrado(request)
    conteo = encuestas.count()
    total = Encuesta.objects.all().count()

    relacion = {}
    for obj in ViveFamilia.objects.all():
        valor = Composicion.objects.filter(encuesta__in=encuestas, relacion_finca_vivienda=obj).count()
        relacion[obj.nombre] = valor

    electricidad = {}
    for obj in EnergiaFinca.objects.all():
        valor = ServiciosBasicos.objects.filter(encuesta__in=encuestas, electricidad=obj).count()
        electricidad[obj.nombre] = valor

    combustible = {}
    for obj in Combustible.objects.all():
        valor = ServiciosBasicos.objects.filter(encuesta__in=encuestas, combustible=obj).count()
        combustible[obj.nombre] = valor

    agua_trabajo = {}
    for obj in AguaFinca.objects.all():
        valor = ServiciosBasicos.objects.filter(encuesta__in=encuestas, agua_trabajo_finca=obj).count()
        agua_trabajo[obj.nombre] = valor

    agua_consumo = {}
    for obj in AguaFinca.objects.all():
        valor = ServiciosBasicos.objects.filter(encuesta__in=encuestas, agua_consumo_humano=obj).count()
        agua_consumo[obj.nombre] = valor

    return render(request, template, locals())

def salida4(request, template='encuesta/salida_a/dependientes.html'):
    encuestas = _query_set_filtrado(request)
    conteo = encuestas.count()
    total = Encuesta.objects.all().count()

    adultos = Composicion.objects.filter(encuesta__in=encuestas).aggregate(cuanto=Avg('adultos'))
    adultas = Composicion.objects.filter(encuesta__in=encuestas).aggregate(cuanto=Avg('adultas'))
    j_varones = Composicion.objects.filter(encuesta__in=encuestas).aggregate(cuanto=Avg('jovenes_varones'))
    j_mujeres = Composicion.objects.filter(encuesta__in=encuestas).aggregate(cuanto=Avg('jovenes_mujeres'))
    ninos = Composicion.objects.filter(encuesta__in=encuestas).aggregate(cuanto=Avg('ninos'))
    ninas = Composicion.objects.filter(encuesta__in=encuestas).aggregate(cuanto=Avg('ninas'))

    h_permanentes = Composicion.objects.filter(encuesta__in=encuestas).aggregate(cuanto=Avg('permanente_hombres'))
    m_permanentes = Composicion.objects.filter(encuesta__in=encuestas).aggregate(cuanto=Avg('permanente_mujeres'))
    h_temporal = Composicion.objects.filter(encuesta__in=encuestas).aggregate(cuanto=Avg('temporales_hombres'))
    m_temporal = Composicion.objects.filter(encuesta__in=encuestas).aggregate(cuanto=Avg('temporales_mujeres'))
    
    return render(request, template, locals())

def salida5(request, template='encuesta/salida_a/conexion.html'):
    encuestas = _query_set_filtrado(request)
    conteo = encuestas.count()
    total = Encuesta.objects.all().count()

    gremial = {}
    for obj in SocioOrganizacion.objects.all():
        valor = QuienFinancia.objects.filter(encuesta__in=encuestas, socio=obj).count()
        gremial[obj.nombre] = valor

    credito = {}
    for obj in CreditoE.objects.all():
        valor = QuienFinancia.objects.filter(encuesta__in=encuestas, tiene_credito=obj).count()
        credito[obj.nombre] = valor

    dequien = {}
    for obj in DeQuien.objects.all():
        valor = QuienFinancia.objects.filter(encuesta__in=encuestas, de_quien=obj).count()
        dequien[obj.nombre] = valor

    comercializan = {}
    for obj in Organizacion.objects.all():
        valor = encuestas.filter(beneficiarios=obj).count()
        comercializan[obj.nombre] = valor
    
    return render(request, template, locals())

def salida6(request, template='encuesta/salida_a/recursos.html'):
    encuestas = _query_set_filtrado(request)
    conteo = encuestas.count()
    total = Encuesta.objects.all().count()

    totalicimo = UsoTierra.objects.filter(encuesta__in=encuestas, tierra__id=1).aggregate(total=Sum('area'))['total']

    tierra = {}
    for obj in Uso.objects.all():
        valor = UsoTierra.objects.filter(encuesta__in=encuestas, tierra=obj).aggregate(total=Sum('area'))['total']
        if valor > 0 :
            tierra[obj.nombre] = valor
    
    reforestacion = {}
    for obj in Actividad.objects.all():
        valor = Reforestacion.objects.filter(encuesta__in=encuestas, reforestacion=obj,respuesta=1).count()
        reforestacion[obj.nombre] = valor
    
    return render(request, template, locals())

def salida7(request, template='encuesta/salida_b/produccion.html'):
    encuestas = _query_set_filtrado(request)
    conteo = encuestas.count()
    total = Encuesta.objects.all().count()

    produccion = collections.OrderedDict()
    for obj in EstadoActual.objects.all():
        doce = AreaCafe.objects.filter(encuesta__in=encuestas, estado=obj).aggregate(total=Sum('doce'))
        trece = AreaCafe.objects.filter(encuesta__in=encuestas, estado=obj).aggregate(total=Sum('trece'))
        catorce = AreaCafe.objects.filter(encuesta__in=encuestas, estado=obj).aggregate(total=Sum('catorse'))
        produccion[obj.nombre] = doce,trece,catorce
    #areas totales
    area_total_doce = AreaCafe.objects.filter(encuesta__in=encuestas, estado__id=1).aggregate(doce=Sum('doce'))
    area_total_trece = AreaCafe.objects.filter(encuesta__in=encuestas, estado__id=1).aggregate(trece=Sum('trece'))
    area_total_catorce = AreaCafe.objects.filter(encuesta__in=encuestas, estado__id=1).aggregate(catorse=Sum('catorse'))
    #producciones
    p_total_doce = AreaCafe.objects.filter(encuesta__in=encuestas, estado__id=4).aggregate(doce=Sum('doce'))
    p_total_trece = AreaCafe.objects.filter(encuesta__in=encuestas, estado__id=4).aggregate(trece=Sum('trece'))
    p_total_catorce = AreaCafe.objects.filter(encuesta__in=encuestas, estado__id=4).aggregate(catorse=Sum('catorse'))
    #pergamino
    pergamino_doce = AreaCafe.objects.filter(encuesta__in=encuestas, estado__id=6).aggregate(doce=Sum('doce'))
    pergamino_trece = AreaCafe.objects.filter(encuesta__in=encuestas, estado__id=6).aggregate(trece=Sum('trece'))
    pergamino_catorce = AreaCafe.objects.filter(encuesta__in=encuestas, estado__id=6).aggregate(catorse=Sum('catorse'))
    #oro
    oro_doce = AreaCafe.objects.filter(encuesta__in=encuestas, estado__id=7).aggregate(doce=Sum('doce'))
    oro_trece = AreaCafe.objects.filter(encuesta__in=encuestas, estado__id=7).aggregate(trece=Sum('trece'))
    oro_catorce = AreaCafe.objects.filter(encuesta__in=encuestas, estado__id=7).aggregate(catorse=Sum('catorse'))
    
    return render(request, template, locals())

def salida75(request, template='encuesta/salida_b/incidencia.html'):
    encuestas = _query_set_filtrado(request)
    conteo = encuestas.count()
    total = Encuesta.objects.all().count()

    incidencias = collections.OrderedDict()
    for obj in Variedades.objects.all():
        plantio = VariedadEdadRoya.objects.filter(encuesta__in=encuestas, variedades=obj).count()
        area = VariedadEdadRoya.objects.filter(encuesta__in=encuestas, variedades=obj).aggregate(area=Sum('area'))['area']
        edad = VariedadEdadRoya.objects.filter(encuesta__in=encuestas, variedades=obj).aggregate(edad=Sum('edad'))['edad']
        try:
            promedio_edad = round(float(edad) / float(plantio),2)
        except:
            promedio_edad = 0
        produccion = VariedadEdadRoya.objects.filter(encuesta__in=encuestas, variedades=obj).aggregate(prod=Sum('produccion_2014'))['prod']
        incidencia = VariedadEdadRoya.objects.filter(encuesta__in=encuestas, variedades=obj).aggregate(incidencia=Sum('nivel_roya'))['incidencia']
        try:
            promedio_incidencia = round(float(incidencia) / float(plantio),2)
        except:
            promedio_incidencia = 0
        try:
            productividad = round(float(produccion) / float(area),2)
        except:
            productividad = 0
        if plantio != 0:
            incidencias[obj.nombre] = (plantio,area,promedio_edad,produccion,promedio_incidencia,productividad)

    return render(request, template, locals())

def salida8(request, template='encuesta/salida_b/vivero.html'):
    encuestas = _query_set_filtrado(request)
    conteo = encuestas.count()
    total = Encuesta.objects.all().count()

    predominante = collections.OrderedDict()
    for obj in VariedadPredominante.objects.all():
        valor = ProduccionVivero.objects.filter(encuesta__in=encuestas, variedad_predomindante=obj).count()
        predominante[obj.nombre] = valor

    vivero_cafe = {}
    for obj in CHOICE_SI_NO:
        valor = ProduccionVivero.objects.filter(encuesta__in=encuestas, vivero_finca=obj[0]).count()
        vivero_cafe[obj[1]] = valor

    min_planta = ProduccionVivero.objects.filter(encuesta__in=encuestas).aggregate(minimo=Min('plantas_vivero'))['minimo']
    max_planta = ProduccionVivero.objects.filter(encuesta__in=encuestas).aggregate(maximo=Max('plantas_vivero'))['maximo']
    total_planta = round(ProduccionVivero.objects.filter(encuesta__in=encuestas).aggregate(total=Avg('plantas_vivero'))['total'],2)
    promedio_sembrar = round(float(total_planta) / float(3500),2)
    area_total_catorce = AreaCafe.objects.filter(encuesta__in=encuestas, estado__id=1).aggregate(catorse=Sum('catorse'))['catorse']
    area_representa = round(promedio_sembrar / float(area_total_catorce),2)

    variedads = {}
    for obj in Variedades.objects.all():
        valor = ProduccionVivero.objects.filter(encuesta__in=encuestas, variedad=obj).count()
        variedads[obj.nombre] = valor

    semilla = {}
    for obj in Semilla.objects.all():
        valor = ProduccionVivero.objects.filter(encuesta__in=encuestas, consigue_semilla=obj).count()
        semilla[obj.nombre] = valor

    decide_sembrar = {}
    for obj in DecideSembrar.objects.all():
        valor = ProduccionVivero.objects.filter(encuesta__in=encuestas, decide=obj).count()
        decide_sembrar[obj.nombre] = valor

    criterios = {}
    for obj in Criterios.objects.all():
        valor = ProduccionVivero.objects.filter(encuesta__in=encuestas, criterio=obj).count()
        criterios[obj.nombre] = valor

    
    return render(request, template, locals())

def salida9(request, template='encuesta/salida_b/autoevaluacion.html'):
    encuestas = _query_set_filtrado(request)
    conteo = encuestas.count()
    total = Encuesta.objects.all().count()

    cafeto = collections.OrderedDict()
    for obj in Manejos.objects.all():
        valor = ManejoCafetales.objects.filter(encuesta__in=encuestas, fecha=3, manejo_cafeto=obj).count()
        cafeto[obj.nombre] = valor

    maleza = collections.OrderedDict()
    for obj in Manejos.objects.all():
        valor = ManejoCafetales.objects.filter(encuesta__in=encuestas, fecha=3, manejo_maleza=obj).count()
        maleza[obj.nombre] = valor

    sombra = collections.OrderedDict()
    for obj in Manejos.objects.all():
        valor = ManejoCafetales.objects.filter(encuesta__in=encuestas, fecha=3, manejo_sombra=obj).count()
        sombra[obj.nombre] = valor

    suelo = collections.OrderedDict()
    for obj in Manejos.objects.all():
        valor = ManejoCafetales.objects.filter(encuesta__in=encuestas, fecha=3, fertilizante_suelo=obj).count()
        suelo[obj.nombre] = valor

    foliares = collections.OrderedDict()
    for obj in Manejos.objects.all():
        valor = ManejoCafetales.objects.filter(encuesta__in=encuestas, fecha=3, fertilizante_foliares=obj).count()
        foliares[obj.nombre] = valor

    fungicida = collections.OrderedDict()
    for obj in Manejos.objects.all():
        valor = ManejoCafetales.objects.filter(encuesta__in=encuestas, fecha=3, fungicidas=obj).count()
        fungicida[obj.nombre] = valor

    insecticida = collections.OrderedDict()
    for obj in Manejos.objects.all():
        valor = ManejoCafetales.objects.filter(encuesta__in=encuestas, fecha=3, insecticidas=obj).count()
        insecticida[obj.nombre] = valor

    nematicida = collections.OrderedDict()
    for obj in Manejos.objects.all():
        valor = ManejoCafetales.objects.filter(encuesta__in=encuestas, fecha=3, nematicidas=obj).count()
        nematicida[obj.nombre] = valor
       
    return render(request, template, locals())

def salida10(request, template='encuesta/salida_b/momentos.html'):
    encuestas = _query_set_filtrado(request)
    conteo = encuestas.count()
    total = Encuesta.objects.all().count()

    cafeto = collections.OrderedDict()
    for obj in Meses.objects.all():
        valor = MesesManejoCafe.objects.filter(encuesta__in=encuestas, fecha=4, mes_manejo_cafeto=obj).count()
        cafeto[obj.nombre] = valor

    maleza = collections.OrderedDict()
    for obj in Meses.objects.all():
        valor = MesesManejoCafe.objects.filter(encuesta__in=encuestas, fecha=4, mes_manejo_maleza=obj).count()
        maleza[obj.nombre] = valor

    sombra = collections.OrderedDict()
    for obj in Meses.objects.all():
        valor = MesesManejoCafe.objects.filter(encuesta__in=encuestas, fecha=4, mes_manejo_sombra=obj).count()
        sombra[obj.nombre] = valor

    suelo = collections.OrderedDict()
    for obj in Meses.objects.all():
        valor = MesesManejoCafe.objects.filter(encuesta__in=encuestas, fecha=4, mes_fertilizante_suelo=obj).count()
        suelo[obj.nombre] = valor

    foliares = collections.OrderedDict()
    for obj in Meses.objects.all():
        valor = MesesManejoCafe.objects.filter(encuesta__in=encuestas, fecha=4, mes_fertilizante_foliares=obj).count()
        foliares[obj.nombre] = valor

    fungicida = collections.OrderedDict()
    for obj in Meses.objects.all():
        valor = MesesManejoCafe.objects.filter(encuesta__in=encuestas, fecha=4, mes_fungicidas=obj).count()
        fungicida[obj.nombre] = valor

    insecticida = collections.OrderedDict()
    for obj in Meses.objects.all():
        valor = MesesManejoCafe.objects.filter(encuesta__in=encuestas, fecha=4, mes_insecticidas=obj).count()
        insecticida[obj.nombre] = valor

    nematicida = collections.OrderedDict()
    for obj in Meses.objects.all():
        valor = MesesManejoCafe.objects.filter(encuesta__in=encuestas, fecha=4, mes_nematicidas=obj).count()
        nematicida[obj.nombre] = valor
       
    return render(request, template, locals())

def salida11(request, template='encuesta/salida_b/insumos.html'):
    encuestas = _query_set_filtrado(request)
    conteo = encuestas.count()
    total = Encuesta.objects.all().count()

    fungicida = {}
    for obj in NombreTipos.objects.all():
        valor = UsoInsumos.objects.filter(encuesta__in=encuestas, tipo=1, nombre=obj).count()
        minimo = UsoInsumos.objects.filter(encuesta__in=encuestas, tipo=1, nombre=obj).aggregate(minimo=Min('aplicaciones'))['minimo']
        maximo = UsoInsumos.objects.filter(encuesta__in=encuestas, tipo=1, nombre=obj).aggregate(maximo=Max('aplicaciones'))['maximo']
        cant_min = UsoInsumos.objects.filter(encuesta__in=encuestas, tipo=1, nombre=obj).aggregate(cant_min=Min('cantidad'))['cant_min']
        cant_max = UsoInsumos.objects.filter(encuesta__in=encuestas, tipo=1, nombre=obj).aggregate(cant_max=Max('cantidad'))['cant_max']
        
        if UsoInsumos.objects.filter(tipo=1, nombre=obj):
            fungicida[obj.nombre] = (valor, minimo, maximo, cant_min, cant_max)

    herbicida = {}
    for obj in NombreTipos.objects.all():
        valor = UsoInsumos.objects.filter(encuesta__in=encuestas, tipo=3, nombre=obj).count()
        minimo = UsoInsumos.objects.filter(encuesta__in=encuestas, tipo=3, nombre=obj).aggregate(minimo=Min('aplicaciones'))['minimo']
        maximo = UsoInsumos.objects.filter(encuesta__in=encuestas, tipo=3, nombre=obj).aggregate(maximo=Max('aplicaciones'))['maximo']
        cant_min = UsoInsumos.objects.filter(encuesta__in=encuestas, tipo=3, nombre=obj).aggregate(cant_min=Min('cantidad'))['cant_min']
        cant_max = UsoInsumos.objects.filter(encuesta__in=encuestas, tipo=3, nombre=obj).aggregate(cant_max=Max('cantidad'))['cant_max']
        
        if UsoInsumos.objects.filter(tipo=3, nombre=obj):
            herbicida[obj.nombre] = (valor, minimo, maximo, cant_min, cant_max)

    insecticidas = {}
    for obj in NombreTipos.objects.all():
        valor = UsoInsumos.objects.filter(encuesta__in=encuestas, tipo=2, nombre=obj).count()
        minimo = UsoInsumos.objects.filter(encuesta__in=encuestas, tipo=2, nombre=obj).aggregate(minimo=Min('aplicaciones'))['minimo']
        maximo = UsoInsumos.objects.filter(encuesta__in=encuestas, tipo=2, nombre=obj).aggregate(maximo=Max('aplicaciones'))['maximo']
        cant_min = UsoInsumos.objects.filter(encuesta__in=encuestas, tipo=2, nombre=obj).aggregate(cant_min=Min('cantidad'))['cant_min']
        cant_max = UsoInsumos.objects.filter(encuesta__in=encuestas, tipo=2, nombre=obj).aggregate(cant_max=Max('cantidad'))['cant_max']
        
        if UsoInsumos.objects.filter(tipo=2, nombre=obj):
            insecticidas[obj.nombre] = (valor, minimo, maximo, cant_min, cant_max)

    fer_suelo = {}
    for obj in NombreTipos.objects.all():
        valor = UsoInsumos.objects.filter(encuesta__in=encuestas, tipo=5, nombre=obj).count()
        minimo = UsoInsumos.objects.filter(encuesta__in=encuestas, tipo=5, nombre=obj).aggregate(minimo=Min('aplicaciones'))['minimo']
        maximo = UsoInsumos.objects.filter(encuesta__in=encuestas, tipo=5, nombre=obj).aggregate(maximo=Max('aplicaciones'))['maximo']
        cant_min = UsoInsumos.objects.filter(encuesta__in=encuestas, tipo=5, nombre=obj).aggregate(cant_min=Min('cantidad'))['cant_min']
        cant_max = UsoInsumos.objects.filter(encuesta__in=encuestas, tipo=5, nombre=obj).aggregate(cant_max=Max('cantidad'))['cant_max']
        
        if UsoInsumos.objects.filter(tipo=5, nombre=obj):
            fer_suelo[obj.nombre] = (valor, minimo, maximo, cant_min, cant_max)

    nematicida = {}
    for obj in NombreTipos.objects.all():
        valor = UsoInsumos.objects.filter(encuesta__in=encuestas, tipo=4, nombre=obj).count()
        minimo = UsoInsumos.objects.filter(encuesta__in=encuestas, tipo=4, nombre=obj).aggregate(minimo=Min('aplicaciones'))['minimo']
        maximo = UsoInsumos.objects.filter(encuesta__in=encuestas, tipo=4, nombre=obj).aggregate(maximo=Max('aplicaciones'))['maximo']
        cant_min = UsoInsumos.objects.filter(encuesta__in=encuestas, tipo=4, nombre=obj).aggregate(cant_min=Min('cantidad'))['cant_min']
        cant_max = UsoInsumos.objects.filter(encuesta__in=encuestas, tipo=4, nombre=obj).aggregate(cant_max=Max('cantidad'))['cant_max']
        
        if UsoInsumos.objects.filter(tipo=4, nombre=obj):
            nematicida[obj.nombre] = (valor, minimo, maximo, cant_min, cant_max)

    abono = {}
    for obj in NombreTipos.objects.all():
        valor = UsoInsumos.objects.filter(encuesta__in=encuestas, tipo=6, nombre=obj).count()
        minimo = UsoInsumos.objects.filter(encuesta__in=encuestas, tipo=6, nombre=obj).aggregate(minimo=Min('aplicaciones'))['minimo']
        maximo = UsoInsumos.objects.filter(encuesta__in=encuestas, tipo=6, nombre=obj).aggregate(maximo=Max('aplicaciones'))['maximo']
        cant_min = UsoInsumos.objects.filter(encuesta__in=encuestas, tipo=6, nombre=obj).aggregate(cant_min=Min('cantidad'))['cant_min']
        cant_max = UsoInsumos.objects.filter(encuesta__in=encuestas, tipo=6, nombre=obj).aggregate(cant_max=Max('cantidad'))['cant_max']
        
        if UsoInsumos.objects.filter(tipo=6, nombre=obj):
            abono[obj.nombre] = (valor, minimo, maximo, cant_min, cant_max)

    foliares = {}
    for obj in NombreTipos.objects.all():
        valor = UsoInsumos.objects.filter(encuesta__in=encuestas, tipo=7, nombre=obj).count()
        minimo = UsoInsumos.objects.filter(encuesta__in=encuestas, tipo=7, nombre=obj).aggregate(minimo=Min('aplicaciones'))['minimo']
        maximo = UsoInsumos.objects.filter(encuesta__in=encuestas, tipo=7, nombre=obj).aggregate(maximo=Max('aplicaciones'))['maximo']
        cant_min = UsoInsumos.objects.filter(encuesta__in=encuestas, tipo=7, nombre=obj).aggregate(cant_min=Min('cantidad'))['cant_min']
        cant_max = UsoInsumos.objects.filter(encuesta__in=encuestas, tipo=7, nombre=obj).aggregate(cant_max=Max('cantidad'))['cant_max']
        
        if UsoInsumos.objects.filter(tipo=7, nombre=obj):
            foliares[obj.nombre] = (valor, minimo, maximo, cant_min, cant_max)
       
    return render(request, template, locals())

def salida12(request, template='encuesta/salida_b/agroecologicas.html'):
    encuestas = _query_set_filtrado(request)
    conteo = encuestas.count()
    total = Encuesta.objects.all().count()

    sanas = [14,9,20,21]
    cultivo = [1,2,8,3,15,17]
    ambiente = [6,7,10,11,12,13]
    plagas = [4,5,16,18,19]

    plantaciones = {}
    for obj in Opciones.objects.filter(id__in=sanas):
        no = UsoOpcionesAgroecologica.objects.filter(encuesta__in=encuestas, opcion=obj, nivel=1).count()
        pequena = UsoOpcionesAgroecologica.objects.filter(encuesta__in=encuestas, opcion=obj, nivel=2).count()
        mayor = UsoOpcionesAgroecologica.objects.filter(encuesta__in=encuestas, opcion=obj, nivel=3).count()
        finca = UsoOpcionesAgroecologica.objects.filter(encuesta__in=encuestas, opcion=obj, nivel=4).count()

        plantaciones[obj.nombre] = (no, pequena, mayor, finca)
    print plantaciones

    fortalecimiento = {}
    for obj in Opciones.objects.filter(id__in=cultivo):
        no = UsoOpcionesAgroecologica.objects.filter(encuesta__in=encuestas, opcion=obj, nivel=1).count()
        pequena = UsoOpcionesAgroecologica.objects.filter(encuesta__in=encuestas, opcion=obj, nivel=2).count()
        mayor = UsoOpcionesAgroecologica.objects.filter(encuesta__in=encuestas, opcion=obj, nivel=3).count()
        finca = UsoOpcionesAgroecologica.objects.filter(encuesta__in=encuestas, opcion=obj, nivel=4).count()
        
        fortalecimiento[obj.nombre] = (no, pequena, mayor, finca)

    mejorar = {}
    for obj in Opciones.objects.filter(id__in=ambiente):
        no = UsoOpcionesAgroecologica.objects.filter(encuesta__in=encuestas, opcion=obj, nivel=1).count()
        pequena = UsoOpcionesAgroecologica.objects.filter(encuesta__in=encuestas, opcion=obj, nivel=2).count()
        mayor = UsoOpcionesAgroecologica.objects.filter(encuesta__in=encuestas, opcion=obj, nivel=3).count()
        finca = UsoOpcionesAgroecologica.objects.filter(encuesta__in=encuestas, opcion=obj, nivel=4).count()
       
        mejorar[obj.nombre] = (no, pequena, mayor, finca)

    supresion = {}
    for obj in Opciones.objects.filter(id__in=plagas):
        no = UsoOpcionesAgroecologica.objects.filter(encuesta__in=encuestas, opcion=obj, nivel=1).count()
        pequena = UsoOpcionesAgroecologica.objects.filter(encuesta__in=encuestas, opcion=obj, nivel=2).count()
        mayor = UsoOpcionesAgroecologica.objects.filter(encuesta__in=encuestas, opcion=obj, nivel=3).count()
        finca = UsoOpcionesAgroecologica.objects.filter(encuesta__in=encuestas, opcion=obj, nivel=4).count()
        
        supresion[obj.nombre] = (no, pequena, mayor, finca)

    
    return render(request, template, locals())

def salida15(request, template='encuesta/salida_d/precio.html'):
    encuestas = _query_set_filtrado(request)
    conteo = encuestas.count()
    total = Encuesta.objects.all().count()

    comercializacion = collections.OrderedDict()
    for obj in CHOICES_ANIOS_comercializacion:
        prod = Comercializacion.objects.filter(encuesta__in=encuestas,
                        fecha=obj[0]).aggregate(prod=Sum('p_total'))['prod']
        i_venta = Comercializacion.objects.filter(encuesta__in=encuestas,
                        fecha=obj[0]).aggregate(i_venta=Sum('i_venta_cafe'))['i_venta']
        i_precio = Comercializacion.objects.filter(encuesta__in=encuestas,
                        fecha=obj[0],i_precio__gt=0).aggregate(i_precio=Avg('i_precio'))['i_precio']
        c_venta = Comercializacion.objects.filter(encuesta__in=encuestas,
                        fecha=obj[0]).aggregate(c_venta=Sum('c_venta'))['c_venta']
        c_precio = Comercializacion.objects.filter(encuesta__in=encuestas,
                        fecha=obj[0],c_precio__gt=0).aggregate(c_precio=Avg('c_precio'))['c_precio']
        e_venta = Comercializacion.objects.filter(encuesta__in=encuestas,
                        fecha=obj[0]).aggregate(e_venta=Sum('e_venta'))['e_venta']
        e_precio = Comercializacion.objects.filter(encuesta__in=encuestas,
                        fecha=obj[0],e_precio__gt=0).aggregate(e_precio=Avg('e_precio'))['e_precio']

        comercializacion[obj[1]] = (prod,i_venta,i_precio,c_venta,c_precio,e_venta,e_precio)


    produccion_11_12 = Comercializacion.objects.filter(encuesta__in=encuestas,
                        fecha=1).aggregate(produccion=Sum('p_total'))['produccion']

    precio1 = Comercializacion.objects.filter(encuesta__in=encuestas,
        fecha=1,i_precio__gt=0).aggregate(precio1=Avg('i_precio'))['precio1']
    precio2 = Comercializacion.objects.filter(encuesta__in=encuestas,
    fecha=1,c_precio__gt=0).aggregate(precio2=Avg('c_precio'))['precio2']
    precio3 = Comercializacion.objects.filter(encuesta__in=encuestas,
    fecha=1,e_precio__gt=0).aggregate(precio3=Avg('e_precio'))['precio3']
    if precio1 == None:
        precio1 = 0
    if precio2 == None:
        precio2 = 0
    if precio3 == None:
        precio3 = 0

    precio_11_12 = (precio1 + precio2 + precio3) / 3
    ingreso_11_12 = produccion_11_12 * precio_11_12

    cambio_volumen = collections.OrderedDict()
    for obj in CHOICES_ANIOS_comercializacion:
        prod = Comercializacion.objects.filter(encuesta__in=encuestas,
                        fecha=obj[0]).aggregate(prod=Sum('p_total'))['prod']
        porcentaje_12 = (produccion_11_12 - prod)*100 / produccion_11_12

        
        i_precio = Comercializacion.objects.filter(encuesta__in=encuestas,
        fecha=obj[0],i_precio__gt=0).aggregate(i_precio=Avg('i_precio'))['i_precio']
        c_precio = Comercializacion.objects.filter(encuesta__in=encuestas,
        fecha=obj[0],c_precio__gt=0).aggregate(c_precio=Avg('c_precio'))['c_precio']
        e_precio = Comercializacion.objects.filter(encuesta__in=encuestas,
        fecha=obj[0],e_precio__gt=0).aggregate(e_precio=Avg('e_precio'))['e_precio']
        if i_precio == None:
            i_precio = 0
        if c_precio == None:
            c_precio = 0
        if e_precio == None:
            e_precio = 0

        precio = (i_precio + c_precio + e_precio) / 3
        
        precio_porcentaje_12 = (precio_11_12 - precio)*100 / precio_11_12
        ingreso = prod * precio
        porcentaje_ingreso = (ingreso_11_12 - ingreso)*100 / ingreso_11_12

        cambio_volumen[obj[1]] = (prod, porcentaje_12,precio,precio_porcentaje_12, 
                                  ingreso, porcentaje_ingreso)


    return render(request, template, locals())

def salida16(request, template='encuesta/salida_d/credito.html'):
    encuestas = _query_set_filtrado(request)
    conteo = encuestas.count()
    total = Encuesta.objects.all().count()

    CHOICES_ANIOS_CREDITO_MODELO = (
            (3, '2013-14'),      
    )

    credito_corto = {}
    for obj in CHOICES_ANIOS_CREDITO_MODELO:
        numero = Credito.objects.filter(encuesta__in=encuestas,fecha=obj[0],monto__gt=0).count()
        monto = Credito.objects.filter(encuesta__in=encuestas,fecha=obj[0],monto__gt=0).aggregate(monto=Sum('monto'))['monto']
        monto_max = Credito.objects.filter(encuesta__in=encuestas,fecha=obj[0],monto__gt=0).aggregate(monto_max=Max('monto'))['monto_max']
        monto_min = Credito.objects.filter(encuesta__in=encuestas,fecha=obj[0],monto__gt=0).aggregate(monto_min=Min('monto'))['monto_min']
        
        credito_corto[obj[1]] = (numero,monto,monto_min,monto_max)

    credito_mediano = {}
    for obj in CHOICES_ANIOS_CREDITO_MODELO:
        numero = Credito.objects.filter(encuesta__in=encuestas,fecha=obj[0],credito_mediano__gt=0).count()
        monto = Credito.objects.filter(encuesta__in=encuestas,fecha=obj[0],credito_mediano__gt=0).aggregate(monto=Sum('credito_mediano'))['monto']
        monto_max = Credito.objects.filter(encuesta__in=encuestas,fecha=obj[0],credito_mediano__gt=0).aggregate(monto_max=Max('credito_mediano'))['monto_max']
        monto_min = Credito.objects.filter(encuesta__in=encuestas,fecha=obj[0],credito_mediano__gt=0).aggregate(monto_min=Min('credito_mediano'))['monto_min']
        
        credito_mediano[obj[1]] = (numero,monto,monto_min,monto_max)

    credito_largo = {}
    for obj in CHOICES_ANIOS_CREDITO_MODELO:
        numero = Credito.objects.filter(encuesta__in=encuestas,fecha=obj[0],credito_largo__gt=0).count()
        monto = Credito.objects.filter(encuesta__in=encuestas,fecha=obj[0],credito_largo__gt=0).aggregate(monto=Sum('credito_largo'))['monto']
        monto_max = Credito.objects.filter(encuesta__in=encuestas,fecha=obj[0],credito_largo__gt=0).aggregate(monto_max=Max('credito_largo'))['monto_max']
        monto_min = Credito.objects.filter(encuesta__in=encuestas,fecha=obj[0],credito_largo__gt=0).aggregate(monto_min=Min('credito_largo'))['monto_min']
        
        credito_largo[obj[1]] = (numero,monto,monto_min,monto_max)

    facilidad = {}
    for obj in CHOICES_ANIOS_FACILIDAD:
        valor = Credito.objects.filter(encuesta__in=encuestas,fecha=3,facilidad=obj[0]).count()
        
        facilidad[obj[1]] = valor

    #cobertura
    area_total_catorce = AreaCafe.objects.filter(encuesta__in=encuestas, estado__id=1).aggregate(catorse=Sum('catorse'))['catorse']
    oro_catorce = AreaCafe.objects.filter(encuesta__in=encuestas, estado__id=7).aggregate(catorse=Sum('catorse'))['catorse']
    c_credito_corto = {}
    for obj in CHOICES_ANIOS_CREDITO_MODELO:
        numero = Credito.objects.filter(encuesta__in=encuestas,fecha=obj[0],monto__gt=0).count()
        monto = Credito.objects.filter(encuesta__in=encuestas,fecha=obj[0],monto__gt=0).aggregate(monto=Sum('monto'))['monto']
        cobertura = round(float(numero) / float(conteo),2) * 100
        monto_cafe = round(float(monto) / float(area_total_catorce),2)
        monto_oro = round(float(monto) / float(oro_catorce),2)
        
        c_credito_corto[obj[1]] = (numero,cobertura,monto_cafe,monto_oro)

    c_credito_mediano = {}
    for obj in CHOICES_ANIOS_CREDITO_MODELO:
        numero = Credito.objects.filter(encuesta__in=encuestas,fecha=obj[0],credito_mediano__gt=0).count()
        monto = Credito.objects.filter(encuesta__in=encuestas,fecha=obj[0],credito_mediano__gt=0).aggregate(monto=Sum('credito_mediano'))['monto']
        try:
            cobertura = round(float(numero) / float(conteo),2) * 100
        except:
            cobertura = 0
        try:
            monto_cafe = round(float(monto) / float(area_total_catorce),2)
        except:
            monto_cafe = 0
        try:
            monto_oro = round(float(monto) / float(oro_catorce),2)
        except:
            monto_oro = 0

        c_credito_mediano[obj[1]] = (numero,cobertura,monto_cafe,monto_oro)

    c_credito_largo = {}
    for obj in CHOICES_ANIOS_CREDITO_MODELO:
        numero = Credito.objects.filter(encuesta__in=encuestas,fecha=obj[0],credito_largo__gt=0).count()
        monto = Credito.objects.filter(encuesta__in=encuestas,fecha=obj[0],credito_largo__gt=0).aggregate(monto=Sum('credito_largo'))['monto']
        if monto == None:
            monto = 0
        try:
            cobertura = round(float(numero) / float(conteo),2) * 100
        except:
            cobertura = 0
        try:
            monto_cafe = round(float(monto) / float(area_total_catorce),2)
        except:
            monto_cafe = 0
        try:
            monto_oro = round(float(monto) / float(oro_catorce),2)
        except:
            monto_oro = 0

        c_credito_largo[obj[1]] = (numero,cobertura,monto_cafe,monto_oro)
    

    return render(request, template, locals())


def _get_view(request, vista):
    if vista in VALID_VIEWS:
        return VALID_VIEWS[vista](request)
    else:
        raise ViewDoesNotExist("Tried %s in module %s Error: View not define in VALID_VIEWS." % (vista, 'encuesta.views'))

VALID_VIEWS = {
    'informacion': salida1,
    'ubicacion': salida2,
    'servicios': salida3,
    'dependientes': salida4,
    'conexion': salida5,
    'recursos': salida6,
    'produccion': salida7,
    'incidencia':salida75,
    'vivero': salida8,
    'autoevaluacion': salida9,
    'momentos': salida10,
    'insumos': salida11,
    'agroecologicos': salida12,
    #faltan las salidas 13,14
    'precio': salida15,
    'credito': salida16,
    }

#utilitario
def get_munis(request):
    '''Metodo para obtener los municipios via Ajax segun los departamentos selectos'''
    ids = request.GET.get('ids', '')
    dicc = {}
    resultado = []
    if ids:
        lista = ids.split(',')    
        for id in lista:
            try:
                departamento = Departamento.objects.get(pk=id)
                municipios = Municipio.objects.filter(departamento__id=departamento.pk).order_by('nombre')
                lista1 = []
                for municipio in municipios:
                    muni = {}
                    muni['id'] = municipio.pk
                    muni['nombre'] = municipio.nombre
                    lista1.append(muni)
                    dicc[departamento.nombre] = lista1
            except:
                pass    
    
    #filtrar segun la organizacion seleccionada
    org_ids = request.GET.get('org_ids', '')
    if org_ids:
        lista = org_ids.split(',')    
        municipios = [encuesta.municipio for encuesta in Encuesta.objects.filter(organizacion__id__in=lista)]
        #crear los keys en el dicc para evitar KeyError
        for municipio in municipios:
            dicc[municipio.departamento.nombre] = []
        
        #agrupar municipios por departamento padre                
        for municipio in municipios:
            muni = {'id': municipio.id, 'nombre': municipio.nombre}
            if not muni in dicc[municipio.departamento.nombre]:
                dicc[municipio.departamento.nombre].append(muni)            
    
    resultado.append(dicc)
        
    return HttpResponse(json.dumps(resultado), mimetype='application/json')

def get_comunies(request):
    ids = request.GET.get('ids', '')
    if ids:
        lista = ids.split(',')
    comunies = Comunidad.objects.filter(municipio__pk__in=lista).order_by('nombre').values('id', 'nombre')

    return HttpResponse(json.dumps(list(comunies)), mimetype='application/json')
    
def get_organi(request):
    ids = request.GET.get('ids', '')
    if ids:
        lista = ids.split(',')    
    municipios = Municipio.objects.filter(departamento__pk__in=lista)
    orgs_id_list = [encuesta.beneficiarios.pk for encuesta in Encuesta.objects.filter(municipio__in=municipios)]    
    organizaciones = Organizacion.objects.filter(pk__in=orgs_id_list).order_by('nombre').values('id', 'nombre_corto')
    
    return HttpResponse(json.dumps(list(organizaciones)), mimetype='application/json')