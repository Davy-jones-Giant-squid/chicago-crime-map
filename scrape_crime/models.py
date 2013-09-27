import math

from django.db import models

class Crime(models.Model):
	
	case_number = models.CharField(max_length=255,null=True, blank='', unique=True)
	description = models.CharField(max_length=255,null=True, blank='')
	domestic = models.BooleanField(default=False)
	date = models.CharField(max_length=255,null=True, blank='')
	arrest = models.BooleanField(default=False)
	district = models.CharField(max_length=255,null=True, blank='')
	neighborhood = models.ForeignKey('Neighborhood', null=True, blank=True)
	primary_type = models.CharField(max_length=255, blank='')
	beat = models.CharField(max_length=255,null=True, blank='')
	ward = models.CharField(max_length=255,null=True, blank='')
	iucr = models.CharField(max_length=255,null=True, blank='')	
	updated_on = models.CharField(max_length=255,null=True, blank='')
	fbi_code = models.CharField(max_length=255,null=True, blank=True)
	crime_coordinates = models.ForeignKey('Coordinates', null=True, blank=True)
	block = models.CharField(max_length=255, null=True, blank='')


	def __unicode__(self):
		return u'Crime case number %s: %s' % (self.case_number, self.primary_type)

	class Meta:
		ordering = ['description']


	def in_range(self, latitude, longitude, distance):
		"""
		Given latitude and longitude numbers, as well as a distance,
		return True, if the latitude and longitude are within `distance`
		units of latitude and longitude of the point given.  Otherwise, 
		return False
		"""
		if not latitude or not longitude or not self.location:
			return False

		if math.sqrt((latitude - self.location.latitude)**2 +
			(longitude - self.location.longitude)**2) < distance:
			return True
		else:
			return False


class Coordinates(models.Model):
	latitude = models.FloatField(null=True, blank=True)
	longitude = models.FloatField(null=True, blank=True)

	def __unicode__(self):
		return u'%s, %s' % (self.latitude, self.longitude)


class Neighborhood(models.Model):
	coordinates = models.ManyToManyField(Coordinates)
	name = models.CharField(max_length=255, default=False, unique=True)
	area_number = models.IntegerField(default=False)

	def __unicode__(self):
		return u'Neighborhood: %s' % (self.name)
