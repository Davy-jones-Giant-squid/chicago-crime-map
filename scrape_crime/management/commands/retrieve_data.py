from django.core.management.base import BaseCommand

import urllib2, urllib
import json
import logging

from scrape_crime.models import Crime, Location


log = logging.getLogger('main')
#This will read the data from the url and hold them in memory
url = urllib2.urlopen('http://data.cityofchicago.org/resource/ijzp-q8t2.json').read()
#this will deserialize the data and return a dictionary
data = json.loads(urllib.unquote(url))

terms = ['case_number', 'description', 'domestic', 'date', 'arrest', 'district',
'location_description', 'primary_type', 'beat', 'ward', 'iucr', 'updated_on', 'fbi_code']

class Command(BaseCommand):
	help = 'Retrieve the data from cityofchicago.org'

	def handle(self, *args, **kwargs):
		log.debug('Retrieving data from cityofchicago.org')

		for datum in data:
			non_unicode_keys = dict((str(k), v) for k, v in datum.iteritems())
			if 'location' in non_unicode_keys:
				location_non_unicode = dict((str(k), v) for k, v in non_unicode_keys['location'].iteritems())
				for i in location_non_unicode:
					if i == 'latitude' or i == 'longitude':
						location_non_unicode[i] = str(location_non_unicode[i])
				loc_obj = Location(block=str(non_unicode_keys['block']), 
					community_area=int(non_unicode_keys['community_area']),**location_non_unicode)
				loc_obj.save()
				
				attribute_dict = dict((k,v) for k, v in non_unicode_keys.iteritems() if k in terms)
				for i in attribute_dict:
					if i != 'domestic' or i != 'arrest':
						attribute_dict[i] = str(attribute_dict[i])
				crime_obj = Crime.objects.create(location=loc_obj, **attribute_dict)
				crime_obj.save()

			else:
				if 'latitude' in non_unicode_keys and 'longitude' in non_unicode_keys:
					loc_obj = Location(block=str(non_unicode_keys['block']), 
						community_area=int(non_unicode_keys['community_area']),
						latitude=str(non_unicode_keys['latitude']),
						longitude=str(non_unicode_keys['longitude']))
					attribute_dict = dict((k,v) for k, v in non_unicode_keys.iteritems() if k in terms)
					for i in attribute_dict:
						if i != 'domestic' or i != 'arrest':
							attribute_dict[i] = str(attribute_dict[i])
					crime_obj = Crime.objects.create(location=loc_obj, **attribute_dict)
					crime_obj.save()
				else:
					loc_obj = Location(block=str(non_unicode_keys['block']), 
						community_area=int(non_unicode_keys['community_area']),
						latitude=None,
						longitude=None)
					attribute_dict = dict((k,v) for k, v in non_unicode_keys.iteritems() if k in terms)
					for i in attribute_dict:
						if i != 'domestic' or i != 'arrest':
							attribute_dict[i] = str(attribute_dict[i])
					crime_obj = Crime.objects.create(location=loc_obj, **attribute_dict)
					crime_obj.save()

