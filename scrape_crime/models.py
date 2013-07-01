from django.db import models

class Crime(models.Model):
	
	case_number = models.CharField(max_length=255,null=True, blank='')
	description = models.CharField(max_length=255,null=True, blank='')
	domestic = models.BooleanField(default=False)
	date = models.CharField(max_length=255,null=True, blank='')
	arrest = models.BooleanField(default=False)
	district = models.CharField(max_length=255,null=True, blank='')
	location = models.ForeignKey('Location', null=True, blank=True)
	location_description = models.CharField(max_length=255,null=True, blank='')
	primary_type = models.CharField(max_length=255, blank='')
	beat = models.CharField(max_length=255,null=True, blank='')
	ward = models.CharField(max_length=255,null=True, blank='')
	iucr = models.CharField(max_length=255,null=True, blank='')	
	updated_on = models.CharField(max_length=255,null=True, blank='')
	fbi_code = models.CharField(max_length=255,null=True, blank=True)


	def __unicode__(self):
		return self.id

	class Meta:
		ordering = ['description']

	
class Location(models.Model):
	latitude = models.FloatField(null=True, blank=True)
	longitude = models.FloatField(null=True, blank=True)
	needs_recoding = models.BooleanField(default=False)
	community_area = models.IntegerField(default=False)
	block = models.CharField(max_length=255, null=True, blank='')

	def __unicode__(self):
		return self.block
