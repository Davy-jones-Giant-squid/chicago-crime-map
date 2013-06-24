from django.db import models

class Crime(models.Model):
	"""
	Model that represents the Chicago crime data API
	"""
	ID = models.IntegerField()
	case_number = models.CharField(max_length=8)
	description = models.CharField(max_length=30)
	domestic = models.BooleanField()
	date = models.DateTimeField()
	arrest = models.BooleanField()
	district = models.CharField(max_length=5)
	location = models.ForeignKey('Location')
	location_description = models.CharField(max_length=30)
	primary_type = models.CharField(max_length=10)
	beat = models.IntegerField(blank=True)
	ward = models.IntegerField( blank=True)
	iucr = models.CharField(max_length=5)	
	updated_on = models.DateTimeField()
	fbi_code = models.CharField(max_length=3)


	def __unicode__(self):
		return self.ID

	
class Location(models.Model):
	latitude = models.DecimalField(max_digits=20, decimal_places=14)
	longitude = models.DecimalField(max_digits=20, decimal_places=14)
	needs_recoding = models.BooleanField()
	community_area = models.IntegerField(blank=True)
	block = models.CharField(max_length=30 )
