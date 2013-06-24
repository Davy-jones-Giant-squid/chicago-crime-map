import urllib2
import json

from django.core.management.base import BaseCommand

from scrape_crime.models import Crime

class Command(BaseCommand):
	def handle(self):
		#This will read the data from the url and hold them in memory
		url = urllib2.urlopen('http://data.cityofchicago.org/resource/ijzp-q8t2.json').read()
		#this will deserialize the data and return a dictionary
		data = json.loads(url)

		for datum in data:
			non_unicode_keys = dict((str(k), v) for k, v in datum.iteritems())
			location_non_unicode = dict((str(k), v) for k, v in non_unicode_keys['location'].iteritems())
			obj = Crime(**non_unicode_keys)
			obj.save()
			"""
			When use json.loads(url), json returns a dictionary with 'u' before key and value.
			However, the dic won't load in model(**kwargs) with the 'u'. Find a way to get rid of
			the 'u' before creating objects.

			Create a function that will turn each value in the dictionary to the right data type
			like:
			dic = {'number': '10'}
			dic['number'] = int(dic['number'])
			>>>dic
			>>>{'number': 10}
			"""



