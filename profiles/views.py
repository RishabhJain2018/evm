from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from braces.views import LoginRequiredMixin

def bad_request_404(request):
	response = render(request, '404.html')
	response.status_code = 404
	return response


def bad_request_500(request):
	response = render(request, '500.html')
	response.status_code = 500
	return response


class Home(View):
	'''
	This is the home page view function.
	'''

	def get(self, request):
		template_name = 'profiles/base.html'
		return render(request, template_name)





