# -*- coding: utf-8 -*-

from django.shortcuts import render
from .models import *

def index(request):
    familias = Encuesta.objects.all().count()
    # if request.method == 'POST':
    #     form1 = MapaForm(request.POST)
    #     if form1.is_valid():
    #         request.session['fecha1'] = form1.cleaned_data['fecha1']   
    # else:
    #     form1 = MapaForm() 

    return render(request, 'index.html', locals())      