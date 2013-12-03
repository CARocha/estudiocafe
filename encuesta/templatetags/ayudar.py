from django import template
register = template.Library()

@register.filter
def porcentaje(fraccion, relleno):    
    try:  
        return "%.2f%%" % ((float(fraccion) / float(relleno)) * 100)  
    except ValueError:  
        return ''