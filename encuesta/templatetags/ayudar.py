from django import template
register = template.Library()

@register.filter
def porcentaje(fraccion, relleno):    
    try:  
        return "%.1f" % ((float(fraccion) / float(relleno)) * 100)  
    except ValueError: 
        return ''

@register.filter
def dividir(valor1, valor2):    
    try:  
        return "%.2f" % ( float(valor1) / float(valor2) )  
    except ValueError:
        return ''