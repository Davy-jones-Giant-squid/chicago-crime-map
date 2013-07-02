from django.http import HttpResponse

from scrape_crime.models import Crime, Location

def map(request):
	coordinates = Location.objects.order_by('id')
	output = ["It happened on: %s.\n" %l.block for l in coordinates]
	return HttpResponse(output)
