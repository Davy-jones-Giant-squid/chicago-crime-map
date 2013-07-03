from django import forms
from django.shortcuts import render_to_response
from gmapi import maps
from gmapi.forms.widgets import GoogleMap

from scrape_crime.models import Crime, Location

class MapForm(forms.Form):
	map = forms.Field(widget=GoogleMap(attrs={'width':510, 'height': 500}))


def map(request):
	myLatlng = maps.LatLng(41.87,-87.62)
	gmap = maps.Map(opts = {
		'center': myLatlng,
		'mapTypeId': maps.MapTypeId.ROADMAP,
		'zoom': 13,
		'mapTpeControlOptions':{
			'style': maps.MapTypeControlStyle.DROPDOWN_MENU
		},
		})

	obj = Crime.objects.order_by('id')
	for i in obj[:10]:
		marker = maps.Marker(opts = {
			'position': maps.LatLng(i.location.latitude, i.location.longitude),
			'map' : gmap,
			})
		maps.event.addListener(marker, 'mouseover','myobj.markerOver')
		maps.event.addListener(marker, 'mouseout', 'myobj.markerOut')
		info = maps.InfoWindow({
			'content': i.primary_type,
			})
		info.open(gmap, marker)
	context = {'form': MapForm(initial={'map':gmap})}
	return render_to_response('map.html', context)
