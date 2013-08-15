import datetime
import json

from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.utils import simplejson

from scrape_crime.models import Crime, Location

def home(request):
	return render_to_response('homepage.html')


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



"""
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
"""