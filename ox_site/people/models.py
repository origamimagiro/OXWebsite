from django.db import models
from django.contrib.auth.admin import User

# Create your models here.

class Brother(models.Model):
	user = models.OneToOneField(User, unique=True) #leverage the base user model
	class_year = models.IntegerField(blank=True)
	major = models.CommaSeparatedIntegerField(max_length=20,blank=True, null=True)
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

	






