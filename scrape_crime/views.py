import datetime
from gmapi import maps
from gmapi.forms.widgets import GoogleMap
import json

from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.utils import simplejson

from scrape_crime.models import Crime, Location

class MapForm(forms.Form):
	map = forms.Field(widget=GoogleMap(attrs={'width':510, 'height': 500}))

def heatmap(request):
	objs = Crime.objects.exclude(location__latitude=None).values('location__latitude', 'location__longitude') 

	#.values(**kwargs) will retrieve object's field value and put them in a list of dictionary, ex:
	#[{'location__longitude': -87.704368230683002, 'location__latitude': 41.821902362679687}, 
	#{'location__longitude': -87.807156332975083, 'location__latitude': 41.945413796757549}, 
	#{'location__longitude': -87.647133449272189, 'location__latitude': 41.935362071404619}, 
	#{'location__longitude': -87.723676565062746, 'location__latitude': 41.814207227378269}]

	list_obj = [[i['location__latitude'], i['location__longitude']] for i in objs]
	#looping through a list is faster than hitting the database at every loop
	cxt = {'obj': list_obj}
	return render_to_response('heatmap.html', cxt)

def markermap(request):
	objs = Crime.objects.exclude(location__latitude=None).values('location__latitude', 'location__longitude', 'primary_type') 
	list_obj = [[i['location__latitude'], i['location__longitude'], str(i['primary_type'])] for i in objs]
	context = {'objects': simplejson.dumps(list_obj)}
	return render_to_response('markermap.html', context)


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