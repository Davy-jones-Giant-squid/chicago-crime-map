from django import forms
from django.shortcuts import render_to_response
from gmapi import maps
from gmapi.forms.widgets import GoogleMap
from django.http import HttpResponse


from scrape_crime.models import Crime, Location

class MapForm(forms.Form):
	map = forms.Field(widget=GoogleMap(attrs={'width':510, 'height': 500}))

def heatmap(request):
	obj = Crime.objects.exclude(location__latitude=None)
	list_obj = []
	for i in obj:
		list_obj.append([i.location.latitude, i.location.longitude])
	cxt = {'obj': list_obj}
	return render_to_response('heatmap.html', cxt)
	

def map(request, latitude=41.87, longitude=-87.62):
	distance = 0.03
	myLatlng = maps.LatLng(latitude, longitude)
	gmap = maps.Map(opts = {
		'center': myLatlng,
		'mapTypeId': maps.MapTypeId.ROADMAP,
		'zoom': 13,
		'mapTpeControlOptions':{
			'style': maps.MapTypeControlStyle.DROPDOWN_MENU
		},
	})


	obj = Crime.objects.filter(location__latitude__gte=latitude - distance,
		location__latitude__lte=latitude + distance, location__longitude__gte=longitude - distance,
		location__longitude__lte=longitude + distance)
	for i in obj:
		if i.in_range(latitude, longitude, distance):
			try:
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
			except AttributeError:
				pass

	context = {'form': MapForm(initial={'map':gmap})}
	return render_to_response('map.html', context)


def map2(request, latitude=41.87, longitude=-87.62):
	distance = 0.03
	objs = Crime.objects.filter(location__latitude__gte=latitude - distance,
		location__latitude__lte=latitude + distance, location__longitude__gte=longitude - distance,
		location__longitude__lte=longitude + distance)
	cxt = {
		'latitude': latitude,
		'longitude': longitude,
		'distance': distance,
		'crimes': objs,
	}

	return render_to_response('map2.html', cxt)