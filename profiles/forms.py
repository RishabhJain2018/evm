from django import forms
from .models import UserDetail
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'email']
        exclude = ['username',]


class UserProfile(forms.ModelForm):

    class Meta:
        model = UserDetail
        exclude = ['user',]