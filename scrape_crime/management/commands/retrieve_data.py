from django.core.management.base import BaseCommand

import urllib2, urllib
import json

from scrape_crime.models import Crime, Neighborhood, Coordinates



#This will read the data from the url and hold them in memory
url = urllib2.urlopen('http://data.cityofchicago.org/resource/ijzp-q8t2.json').read()
#this will deserialize the data and return a dictionary
data = json.loads(urllib.unquote(url))


bool_terms = ['domestic', 'arrest']
terms_type = {
	'case_number': str,
	'description': str, 
	'date': str, 
	'district': str,
	'primary_type': str, 
	'beat': str,
	'ward': str, 
	'iucr': str, 
	'updated_on': str, 
	'fbi_code': str,
	'latitude': float,
	'longitude': float,
	'community_area': int,
	'block': str
}
def make_dict(unordered_dict):
	"""
	This function returns a dictionary that matches the attributes needed 
	to create a crime object.
	"""
	dict_for_obj = {
		'crime_list': {},
		'crime_coordinates':{}
	}


	crime_list = [
				'case_number', 
				'description', 
				'domestic',
				'date',
				'arrest', 
				'district',
				'primary_type', 
				'beat', 
				'ward', 
				'iucr', 
				'updated_on', 
				'fbi_code',
				'block'
			]


	crime_coordinates = ['latitude', 'longitude']

	for i in unordered_dict:
		if i == "latitude" or i == 'longitude':
			dict_for_obj['crime_coordinates'][i] = unordered_dict[i]
		elif i == 'community_area':
			dict_for_obj[i] = unordered_dict[i]
		else:
			dict_for_obj['crime_list'][i] = unordered_dict[i]
	return dict_for_obj


def unicode_to_type(unicode_dict):
	"""
	This function convert the unicode value from the dictionary argument
	into the right type for the model. It returns a dict with values of the 
	type listed in terms_type.
	"""

	new_type_dict = dict((k, v) for k, v in unicode_dict.iteritems() if k in terms_type or k in bool_terms)

	for keyword in new_type_dict:
		if keyword in terms_type:
			new_type_dict[keyword] = terms_type[keyword](new_type_dict[keyword])
	
	return new_type_dict


def make_crime(attributes_dict):
	for crime in attributes_dict:
		try:
			crime_obj = Crime.objects.get(case_number=attributes_dict['crime_list']['case_number'])
		except Crime.DoesNotExist:
			coordinates_obj = Coordinates(**attributes_dict['crime_coordinates'])
			coordinates_obj.save()
			neighborhood_obj = Neighborhood.objects.get(area_number=attributes_dict['community_area'])
			crime_obj= Crime.objects.create(crime_coordinates=coordinates_obj,neighborhood=neighborhood_obj, **attributes_dict['crime_list'])
			
		return crime_obj

class Command(BaseCommand):
	help = 'Retrieve the data from cityofchicago.org'

	def handle(self, *args, **kwargs):

		num_of_id = 0
		"""
		Each datum represent a dictionary whose keys and values are in unicode, for example:
		{
			u'community_area': u'14', # Int
			u'primary_type': u'THEFT', # Str
			u'beat': u'1713',  # Int
			u'year': u'2013', # Int
			u'domestic': False, # Bool
			u'iucr': u'0820', # Str
			u'arrest': False, # Bool
			u'location_description': 
			u'VEHICLE NON-COMMERCIAL', 
			u'case_number': u'HW444620', 
			u'date': u'2013-09-09T05:00:00', #Datetime "%Y-%m-%dT%h:%n%s"
			u'updated_on': u'2013-09-15T00:39:58', 
			u'ward': u'33', 
			u'fbi_code': u'06', 
			u'id': u'9305010', 
			u'block': u'030XX W ARGYLE ST', 
			u'description': u'$500 AND UNDER'
		}

		"""
		for datum in data:
			num_of_id += 1
			# non_unicode_keys return a dictionary whose keys are strings, but values remain
			# unicode
			non_unicode_keys = dict((str(k), v) for k, v in datum.iteritems())
			try:
				type_keys = unicode_to_type(non_unicode_keys)
			except KeyError:
				pass
			ordered_dict = make_dict(type_keys)
			crime_object = make_crime(ordered_dict)
			print crime_object, crime_object.neighborhood
		print num_of_id