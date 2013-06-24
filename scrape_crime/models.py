from django.db import models

class Crime(models.Model):
	"""
	Model that represents the Chicago crime data API
	"""
	ID = models.IntegerField(null=True, blank=True)
	case_number = models.CharField(max_length=8, default='')
	x_coordinate = models.IntegerField(null=True, blank=True)
	y_coordinate = models.IntegerField(null=True, blank=True)
	description = models.CharField(max_length=30, null=False)
	domestic = models.BooleanField()
	date = models.DateTimeField()
	year = models.IntegerField(null=True, blank=True)
	arrest = models.BooleanField()
	district = models.CharField(max_length=5, null=False)
	location = models.ForeignKey('Location')
	location_description = models.CharField(max_length=30, null=False)
	community_area = models.IntegerField(null=True, blank=True)
	primary_type = models.CharField(max_length=10, null=False)
	beat = models.IntegerField(null=True, blank=True)
	ward = models.IntegerField(null=True, blank=True)
	iucr = models.CharField(max_length=5, null=False)	
	updated_on = models.DateTimeField()
	fbi_code = models.CharField(max_length=3, null=False)
	block = models.CharField(max_length=30, null=False)


	def __unicode__(self):
		return self.ID

	
class Location(models.Model):
	latitude = models.DecimalField(max_digits=20, decimal_places=14)
	longitude = models.DecimalField(max_digits=20, decimal_places=14)
	needs_recoding = models.BooleanField()
