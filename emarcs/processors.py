'''
Created on 24/feb/2014

@author: Marco Pompili
'''

from django.conf import settings as django_settings

def on_debug(request):
    return { 'on_debug' : django_settings.DEBUG }