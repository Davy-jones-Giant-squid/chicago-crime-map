from django.core.management.base import BaseCommand

from scrape_crime.models import Neighborhood, Coordinates

from xml.dom import minidom

xmldoc = minidom.parse("scrape_crime/management/commands/Kmlcommunityareas.kml.kml")
document = xmldoc.getElementsByTagName("Document")[0]
placemarks = document.getElementsByTagName("Placemark")
community_area = {
		'near south side': 33, 'near west side': 28, 'mount greenwood': 74, 
		'grand boulevard': 38, 'washington heights': 73, 'montclare': 18, 
		'woodlawn': 42, 'dunning': 17, 'norwood park': 10, 'north lawndale': 29, 
		'logan square': 22, 'humboldt park': 23, 'lincoln park': 7, 'uptown': 3, 
		'oakland': 36, 'pullman': 50, 'burnside': 47, 'washington park': 40, 
		'new city': 61, 'lincoln square': 4, 'south lawndale': 30, 'loop': 32, 
		'west elsdon': 62, 'south shore': 43, 'clearing': 64, 'west pullman': 53, 
		'morgan park': 75, 'lake view': 6, 'douglas': 35, 'west garfield park': 26, 
		'kenwood': 39, 'east garfield park': 27, 'south deering': 51, "ohare": 76, 
		'gage park': 63, 'hermosa': 20, 'mckinley park': 59, 'calumet heights': 48, 
		'rogers park': 1, 'north park': 13, 'roseland': 49, 'hegewisch': 55, 
		'greater grand crossing': 69, 'auburn gresham': 71, 'belmont cragin': 19, 
		'edison park': 9, 'south chicago': 46, 'hyde park': 41, 'forest glen': 12, 
		'fuller park': 37, 'near north side': 8, 'jefferson park': 11, 
		'north center': 5, 'avondale': 21, 'chatham': 44, 'avalon park': 45, 
		'garfield ridge': 56, 'portage park': 15, 'ashburn': 70, 'albany park': 14, 
		'englewood': 68, 'east side': 52, 'bridgeport': 60, 'west lawn': 65, 
		'west ridge': 2, 'irving park': 16, 'edgewater': 77, 'armour square': 34, 
		'brighton park': 58, 'lower west side': 31, 'west englewood': 67, 
		'archer heights': 57, 'beverly': 72, 'riverdale': 54, 'austin': 25, 
		'chicago lawn': 66, 'west town': 24
		}

class Command(BaseCommand):
	help = 'Retrieve the coordinates of Chicago neighborhoods'

	def handle(self, *args, **kwargs):
		for placemark in placemarks:
			description = placemark.getElementsByTagName('description')[0].firstChild.data
			name = description.split("<")
			neighborhood_name = str((name[20][3:]).lower())
			neighborhood_obj = Neighborhood(name=neighborhood_name, area_number=community_area[neighborhood_name])
			neighborhood_obj.save()
			print "Saving coordinates for: %s" % neighborhood_name
			#firstChild.data returns whatever lies between the beginning and ending tag selected
			raw_coordinates = placemark.getElementsByTagName("coordinates")[0].firstChild.data
			# lst returns sets of coordinates that are separated by a space.
			# NB: starts at [1] because [0] is a " ".
			lst = raw_coordinates[1:].split(" ")
			# coordinate separate each coordinates
			for l in lst:
				coordinate = l.split(",")
				del coordinate[-1]
				longi = float(coordinate[0])
				lati = float(coordinate[1])
				coord_obj = Coordinates(latitude=lati, longitude=longi)
				coord_obj.save()
				neighborhood_obj.coordinates.add(coord_obj)

