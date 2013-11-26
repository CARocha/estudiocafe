from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns('encuesta.views',
    url(r'^$', 'index', name="index"),
    #url(r'^proyecto/$', 'proyecto'),
    )