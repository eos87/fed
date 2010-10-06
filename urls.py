from django.conf.urls.defaults import *
from django.contrib import admin


admin.autodiscover()

import os
PROJECT_DIR = os.path.dirname(__file__)

urlpatterns = patterns('',
    (r'^files/(?P<path>.*)$', 'django.views.static.serve', {'document_root': PROJECT_DIR + '/files'}),
    (r'^$','fed.encuesta.views.index'),
    (r'^', include('fed.encuesta.urls')),
    
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}),
    (r'^admin/', include(admin.site.urls)),
)
