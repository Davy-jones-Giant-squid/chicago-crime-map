from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',


    (r'^$', 'scrape_crime.views.map'),
    (r'^2$', 'scrape_crime.views.map2'),
    (r'^heatmap/', 'scrape_crime.views.heatmap'),
    (r'^markermap/', 'scrape_crime.views.markermap'),
    # url(r'^chicagocrime/', include('chicagocrime.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
