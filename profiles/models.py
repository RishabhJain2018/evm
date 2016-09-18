from django.db import models
from django.contrib.auth.models import User


class UserDetail(models.Model):
    '''
    It stores information about the users.
    '''
    user = models.OneToOneField(User)
    github = models.CharField(max_length=200, blank=False, null=False)
    linkedin = models.CharField(max_length=200, blank=False, null=False)
    contact_no = models.CharField(max_length=200, blank=False, null=False)
    about = models.CharField(max_length=500, blank=False, null=False)

    created = models.DateTimeField("Created", null=True, auto_now_add=True)
    modified = models.DateTimeField("Last Modified", null=True, auto_now=True)

    def __unicode__(self):
        return self.user.username
