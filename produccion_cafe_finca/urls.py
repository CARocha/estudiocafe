from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns('produccion_cafe_finca.views',
    (r'^c/(?P<vista>[-\w]+)/$', '_get_view'),
    (r'^g/(?P<vista>[-\w]+)/$', '_get_view'),
  
    )