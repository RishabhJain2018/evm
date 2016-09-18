from django.conf.urls import include, url
from django.contrib import admin
from .views import Dashboard

urlpatterns = [
	url(r'^dashboard/$', Dashboard.as_view(), name='dashboard'),

]