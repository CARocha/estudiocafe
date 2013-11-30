# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from encuesta.models import *
from lugar.models import *
from produccion_cafe_finca.models import *

def get_anios():
    years = []
    for en in Encuesta.objects.order_by('fecha__year').values_list('fecha__year', flat=True):
        years.append((en, en))
    return list(set(years))

CHOICE_EDUCACION = (
            ('', '------'),
            (1, 'NSLE'),
            (2, 'PRIn'),
            (3, 'PRC'),
            (4, 'SECIN'),
            (5, 'Bach'),
            (6, 'Univ'),
    )
def departamentos():   
    return Encuesta.objects.all().order_by('municipio__departamento__nombre').distinct().values_list('municipio__departamento__id', 'municipio__departamento__nombre')

class ConsultarForm(forms.Form):
    #anio = forms.ChoiceField(choices=get_anios(), label=u'Año')
    departamento = forms.MultipleChoiceField(choices=departamentos(), required=False, label=u'Departamentos')
    municipio = forms.ModelMultipleChoiceField(queryset=Municipio.objects.all().order_by('nombre'), required=False)
    comunidad = forms.ModelMultipleChoiceField(queryset=Comunidad.objects.all(), required=False)
    altitud = forms.CharField(required=False)
    empresa = forms.ModelMultipleChoiceField(queryset=Organizacion.objects.all().order_by('nombre'), 
                                                                                required=False, label=u'Empresa')
    area_desde = forms.CharField(required=False)
    area_hasta = forms.CharField(required=False)
    area_cafe_desde = forms.CharField(required=False)
    area_cafe_hasta = forms.CharField(required=False)
    escolaridad = forms.ChoiceField(choices=CHOICE_EDUCACION, required=False)
    variedad_predominate = forms.ModelChoiceField(queryset=VariedadPredominante.objects.order_by('nombre'), 
                                                required=False)
    variedad_viviero = forms.ModelChoiceField(queryset=Variedades.objects.order_by('nombre'),
                                                required=False)