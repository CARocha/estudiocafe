from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns('encuesta.views',
    url(r'^$', 'index', name="index"),
    url(r'^consultar/$', 'consultar', name="consultar"),
    url(r'^indicadores/$', 'indicadores', name="indicadores"),
    url(r'^ajax/organi/$', 'get_organi'),
    url(r'^ajax/munis/$', 'get_munis'),
    url(r'^ajax/comunies/$', 'get_comunies'),
    (r'^a/(?P<vista>[-\w]+)/$', '_get_view'),
    )