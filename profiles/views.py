from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

# Create your views here.

class Home(View):
	'''
	This is the home page view function.
	'''
	def get(self, request):
		return render(request,'profiles/base.html')

