from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
	event_name = models.CharField(max_length=200, blank=False, null=False)
	event_description = models.CharField(max_length=200, blank=False, null=False)
	event_location = models.CharField(max_length=200, blank=False, null=False)
	event_start = models.DateTimeField()
	event_end = models.DateTimeField()
	event_poster = models.ImageField()

	def __unicode__(self):
		return self.event_name
