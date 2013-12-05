from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns('roya.views',
    (r'^e/(?P<vista>[-\w]+)/$', '_get_view'),
  
    )