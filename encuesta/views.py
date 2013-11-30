# -*- coding: utf-8 -*-

from django.shortcuts import render
from .models import *

def index(request):
    familias = Encuesta.objects.all().count()

    return render(request, 'index.html', locals())

def consultar(request, template="encuesta/consultar.html"):
    
    return render(request, template, locals())   