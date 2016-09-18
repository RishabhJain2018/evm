from django.contrib.auth.models import User
from profiles.models import UserDetail
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def user_profile_complete(function):
	'''
	Decorator to check that user profile is complete or not.
	'''
	def wrapper(request, *args, **kwargs):
		try:
			user = User.objects.get(username=request.user.username)
			profile = UserDetail.objects.get(user=user)
		except:
			return function(request, *args, **kwargs)

	if user.first_name == "" or user.last_name == "" or user.email == "" or user.github == "" or user.linkedin == "" or user.contact_no == "":
		return HttpResponseRedirect(reverse("user-profile", kwargs={'user_id': str(request.user.username)}))
	else:
		return function(request, *args, **kwargs)
	return wrapper
