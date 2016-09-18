from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from braces.views import LoginRequiredMixin
from allauth.account.views import SignupView
from allauth.account.forms import LoginForm


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
        template_name = 'index.html'
        return render(request, template_name)


class Blog(View):
    '''
    This is the Blog View.
    '''

    def get(self, request):
        template_name = 'blog.html'
        return render(request, template_name)


class About_us(View):
    '''
    This is the about us view.
    '''

    def get(self, request):
        template_name = 'about.html'
        return render(request, template_name)


class Events(View):
    '''
    This is the Events View.
    '''

    def get(self, request):
        template_name = 'events.html'
        return render(request, template_name)


class Dashboard(LoginRequiredMixin, View):
    '''
    This is the Dashboard View.
    '''

    def get(self, request):
        template_name = 'profiles/dashboard.html'
        return render(request, template_name)
