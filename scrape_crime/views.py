from django import forms
from django.shortcuts import render_to_response
from gmapi import maps
from gmapi.forms.widgets import GoogleMap

from scrape_crime.models import Crime, Location

class MapForm(forms.Form):
	map = forms.Field(widget=GoogleMap(attrs={'width':510, 'height': 500}))


def map(request):
	gmap = maps.Map(opts = {
		'center': maps.LatLng(41.87,-87.62),
		'mapTypeId': maps.MapTypeId.ROADMAP,
		'zoom': 11,
		'mapTpeControlOptions':{
			'style': maps.MapTypeControlStyle.DROPDOWN_MENU
		},
		})
	context = {'form': MapForm(initial={'map':gmap})}
	return render_to_response('map.html', context)
