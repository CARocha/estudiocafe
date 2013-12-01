# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from .forms import *
import json

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
            if request.session['comunidad']:
                params['comunidad__in'] = request.session['comunidad']
            else:
                params['municipio__in'] = request.session['municipio']

    if request.session['empresa']:
        params['beneficiarios__in'] = request.session['empresa']
    
    if request.session['altitud']:
        params['altitud'] = request.session['altitud']
        
    if request.session['area_desde']:
        params['usotierra__area__range'] = (request.session['area_desde'],request.session['area_hasta'])

    if request.session['escolaridad']:
        params['escolaridad'] = request.session['escolaridad']

    if request.session['estado_civil']:
        params['estado_civil'] = request.session['estado_civil']


    

    if request.session['iglesia']:
        params['iglesia'] = request.session['iglesia']

    if request.session['importancia']:
        params['importancia_religion'] = request.session['importancia']

    encuestas = Encuesta.objects.filter( ** params)
    return encuestas

def consultar(request, template="encuesta/consultar.html"):
    if request.method == 'POST':
        form = ConsultarForm(request.POST)
        if form.is_valid():
            #request.session['anio'] = form.cleaned_data['anio']
            request.session['departamento'] = form.cleaned_data['departamento']
            request.session['municipio'] = form.cleaned_data['municipio']
            request.session['comunidad'] = form.cleaned_data['comunidad']            
            request.session['altitud'] = form.cleaned_data['altitud']
            request.session['empresa'] = form.cleaned_data['empresa']
            request.session['area_desde'] = form.cleaned_data['area_desde']
            request.session['area_hasta'] = form.cleaned_data['area_hasta']
            request.session['area_cafe_desde'] = form.cleaned_data['area_cafe_desde']  
            request.session['area_cafe_hasta'] = form.cleaned_data['area_cafe_hasta']
            request.session['escolaridad'] = form.cleaned_data['escolaridad']
            request.session['variedad_predominate'] = form.cleaned_data['variedad_predominate']
            request.session['variedad_viviero'] = form.cleaned_data['variedad_viviero']

            request.session['centinel'] = 1
            encuestas = 1#_query_set_filtrado(request).count()
            if encuestas != 0:
                return HttpResponseRedirect('/indicadores/')
            else:
                nono = 2
    else:
        form = ConsultarForm()       
    return render(request, template, locals())

def indicadores(request, template='encuesta/indicadores.html'):
    encuestas = 1#_query_set_filtrado(request)
    return render(request,template, locals())

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