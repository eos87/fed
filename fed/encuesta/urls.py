from django.conf.urls.defaults import *

urlpatterns = patterns('fed.encuesta.views',
    (r'^influencia/$', 'influencia'),
    (r'^indicadores/$', 'indicadores'),
    (r'^indicadores/(?P<vista>[-\w]+)/$', '_get_view'),
)


