from django.db import models
from django.contrib.auth.admin import User
from ox_site import settings
from s3utils import S3CustomStorage


class Brother(models.Model):
	user = models.OneToOneField(User, unique=True) #leverage the base user model
	image = models.ImageField(default=STATIC_URL+'images/coatarms.jpg', storage=S3CustomStorage())
	class_year = models.IntegerField(blank=True)
	major = models.CharField(max_length=20,blank=True, default="undecided")
	hometown = models.CharField(max_length=100, blank=True)
	about = models.CharField(max_length=500, blank=True)
	campus_involvement = models.CharField(max_length=500, blank=True)
	is_alum = models.BooleanField(default=False)
	big_brother = models.ManyToManyField('self', blank=True) # Many to Many with self


	"""
	potential future functionality

	housing_points = models.FloatField(default=0)
	outstanding_balance = models.FloatField(default=0)
	"""

	def __str__(self):
		return self.user.first_name + ' ' + self.user.last_name + ', ' + str(self.class_year)

	






