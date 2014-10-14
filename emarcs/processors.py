"""
Created on 24/feb/2014

@author: Marco Pompili
"""

from django.conf import settings as django_settings


def debugging(request):
    return { 'debugging' : django_settings.DEBUG }