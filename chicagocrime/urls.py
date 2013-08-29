
from django.conf.urls import *


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	#the 'name' option is used for the href block in html
    url(r'^$', 'scrape_crime.views.home', name='homepage'),
    url(r'^heatmap/', 'scrape_crime.views.heatmap', name='heatmap'),
    url(r'^markermap/', 'scrape_crime.views.markermap', name='markermap'),
    # url(r'^chicagocrime/', include('chicagocrime.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
