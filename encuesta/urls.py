from django.conf.urls.defaults import *

urlpatterns = patterns('fed.encuesta.views',
    (r'^influencia/$', 'influencia'),
    (r'^indicadores/$', 'indicadores'),
    (r'^lista/$', 'lista'),
    (r'^lista/(?P<id>\d+)/$', 'lista'),
    (r'^proyecto/(?P<id>\d+)/$', 'proyecto'),
    (r'^organizacion/(?P<id>\d+)/$', 'organizacion'),
    (r'^indicadores/(?P<vista>[-\w]+)/$', '_get_view'),
)


