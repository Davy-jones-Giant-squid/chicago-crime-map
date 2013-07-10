from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    (r'', include('gmapi.urls.media')),
    (r'^$', 'scrape_crime.views.map'),
    (r'^2$', 'scrape_crime.views.map2'),
    (r'^heatmap/', 'scrape_crime.views.heatmap'),
    # url(r'^chicagocrime/', include('chicagocrime.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
