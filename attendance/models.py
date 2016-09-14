from django.db import models
from django.contrib.auth.models import User
from event.models import Event


class Attendance(models.Model):
	user = models.ForeignKey(User)
	event = models.ForeignKey(Event)

	def __unicode__(self):
		return self.user
