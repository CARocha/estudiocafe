# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .forms import *

def index(request):
    familias = Encuesta.objects.all().count()

    return render(request, 'index.html', locals())

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