from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

import os
PROJECT_DIR = os.path.dirname(__file__)

urlpatterns = patterns('',
    (r'^files/(?P<path>.*)$', 'django.views.static.serve', {'document_root': PROJECT_DIR + '/files'}),
    (r'^admin/', include(admin.site.urls)),
)
