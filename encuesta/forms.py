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

CHOICE_ALTITUD = (
            ('', '-----'),
            (1, '400-800'),
            (2, '801-1200'),
            (3, 'Más de 1201'),
    )

CHOICE_AREA_FINCA = (
            ('', '------'),
            (1, '1-10 mz'),
            (2, '11-50 mz'),
            (3, 'Más de 50'),
    )

CHOICE_AREA_CAFE = (
             ('', '------'),
            (1, '1-10 mz'),
            (2, '11-50 mz'),
            (3, 'Más de 50'),
    )

CHOICE_REDUCCION = (
             ('', '------'),
            (1, '0% - 10%'),
            (2, '11% - 30%'),
            (3, 'Más de 31%'),
    )


class ConsultarForm(forms.Form):
    #anio = forms.ChoiceField(choices=get_anios(), label=u'Año')
    departamento = forms.MultipleChoiceField(choices=departamentos(), required=False, label=u'Departamentos')
    municipio = forms.ModelMultipleChoiceField(queryset=Municipio.objects.all().order_by('nombre'), required=False)
    #comunidad = forms.ModelMultipleChoiceField(queryset=Comunidad.objects.all(), required=False)
    altitud = forms.ChoiceField(choices=CHOICE_ALTITUD,required=False)
    empresa = forms.ModelMultipleChoiceField(queryset=Organizacion.objects.all().order_by('nombre'), 
                                                                                required=False, label=u'Empresa')
    area_finca = forms.ChoiceField(choices=CHOICE_AREA_FINCA, required=False)
    area_cafe = forms.ChoiceField(choices=CHOICE_AREA_CAFE, required=False)
    nivel_educacion = forms.ChoiceField(choices=CHOICE_EDUCACION, required=False)
    variedad_predominate = forms.ModelChoiceField(queryset=VariedadPredominante.objects.order_by('nombre'), 
                                                required=False)
    variedad_viviero = forms.ModelChoiceField(queryset=Variedades.objects.order_by('nombre'),
                                                required=False)
    reduccion_cosecha = forms.ChoiceField(choices=CHOICE_REDUCCION,required=False)
    credito = forms.ModelChoiceField(queryset=CreditoE.objects.all(),required=False)