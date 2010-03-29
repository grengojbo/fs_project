# -*- mode: python; coding: utf-8; -*-  
from django.conf.urls.defaults import *

import grappelli
from os.path import join, dirname
from django.conf import settings

from fsa.urls import urlpatterns as fsapatterns

# from django.contrib import admin as adm
# from fsa.core.admin import user_site
# from fsa.core import admin
#adm.autodiscover()


from fsa.admin import admin
admin.site.collections = {
    0: {
        'title': 'User Admin',
        'groups': [0,1]
    },
}


adminpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^grappelli/', include('grappelli.urls')),
    #(r'^adm/(.*)', adm.site.root),
    #(r'^admin/(.*)', user_site.root),
    #(r'^admin/(.*)', admin.site.root),
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns = getattr(settings, 'URLS', [])
if urlpatterns:
    urlpatterns += adminpatterns + fsapatterns
else:
    urlpatterns = adminpatterns + fsapatterns

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    )
urlpatterns += patterns('',
    ('^$', 'django.views.generic.simple.redirect_to', {'url': '/admin/'}),
#    #url(r'^admin-media/(.*)$', 'django.views.static.serve', {'document_root': join(dirname(admin.__file__), 'media')}),
#    url(r'^admin-media/(.*)$', 'django.views.static.serve', {'document_root': join(dirname(grappelli.__path__[0]), 'grappelli/media')}),
#    url(r'^grappelli/', include('grappelli.urls')),
)