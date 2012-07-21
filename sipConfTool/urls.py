from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^sipConfTool/', include('sipConfTool.foo.urls')),
    (r'^admin/sync', 'sip.views.sync'),
    (r'^admin/write', 'sip.views.writeSipConf'),
    (r'^admin/show', 'sip.views.show'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
