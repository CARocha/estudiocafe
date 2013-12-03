# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from .forms import ConsultarForm
import json
from lugar.models import Departamento, Comunidad
from django.db.models import Avg, Sum
from produccion_finca.models import *
from produccion_cafe_finca.models import *
from roya.models import *
from vulnerabilidades_finca.models import *
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
        params['produccionvivero__variedad_predomindante'] = request.session['variedad_predominate']


    if request.session['variedad_viviero']:
        params['produccionvivero__variedad'] = request.session['variedad_viviero']

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

    totalicimo = UsoTierra.objects.filter(encuesta__in=encuestas, tierra__id=1).aggregate(total=Sum('area'))
    
    tierra = {}
    for obj in Uso.objects.all():
        valor = UsoTierra.objects.filter(encuesta__in=encuestas, tierra=obj).aggregate(total=Sum('area'))
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