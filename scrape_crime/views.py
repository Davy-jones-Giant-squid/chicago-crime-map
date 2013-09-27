import datetime
import json

from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.utils import simplejson

from scrape_crime.models import Crime, Neighborhood, Coordinates

def home(request):
	return render_to_response('homepage.html')


def heatmap(request):
	objs = Crime.objects.exclude(crime_coordinates__latitude=None).values('crime_coordinates__latitude', 'crime_coordinates__longitude') 
	list_obj = [[i['crime_coordinates__latitude'], i['crime_coordinates__longitude']] for i in objs]
	#looping through a list is faster than hitting the database at every loop
	cxt = {'obj': list_obj}
	return render_to_response('heatmap.html', cxt)

def markermap(request):
	objs = Crime.objects.exclude(crime_coordinates__latitude=None).values(
		'crime_coordinates__latitude', 'crime_coordinates__longitude', 'primary_type', 'description', 'neighborhood__area_number') 
	neighs = Neighborhood.objects.all()
	neigh_obj = {}
	for neighbor in neighs:
		name = neighbor.name
		area = neighbor.area_number
		coord = [[j.latitude, j.longitude] for j in neighbor.coordinates.all()]
		neigh_obj[name] = [area, coord]
	list_obj = [[i['crime_coordinates__latitude'], i['crime_coordinates__longitude'], str(i['primary_type']), str(i['description']), int(i['neighborhood__area_number'])] for i in objs]
	context = {'objects': simplejson.dumps(list_obj),
				'neighborhood': simplejson.dumps(neigh_obj)
				}
	obj_array = []

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