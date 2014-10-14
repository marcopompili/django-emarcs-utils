__author__ = 'Marco Pompili'


from django import template
from django.conf import settings

register = template.Library()


# To use defaults include this and
# uncomment into your settings.py file
#DEFAULT_BOOTSTRAP = '3.2.0'
#DEFAULT_FONTAWESOME = '4.2.0'
#DEFAULT_JQUERY = '1.11.1'
#DEFAULT_MODERNIZR = '2.8.3'
#DEFAULT_MOOTOOLS = '1.5.1'
#DEFAULT_HTML5SHIV = '3.7.2'


@register.inclusion_tag('emarcs/lib/css/bootstrap3.html')
def bootstrap3_css(**kwargs):
    return {
        'version': kwargs.get('version', settings.DEFAULT_BOOTSTRAP)
    }


@register.inclusion_tag('emarcs/lib/js/bootstrap3.html')
def bootstrap3_js(**kwargs):
    return {
        'version': kwargs.get('version', settings.DEFAULT_BOOTSTRAP)
    }


@register.inclusion_tag('emarcs/lib/css/fontawesome4.html')
def fontawesome(**kwargs):
    return {
        'version': kwargs.get('version', settings.DEFAULT_FONTAWESOME)
    }


@register.inclusion_tag('emarcs/lib/js/jquery.html')
def jquery(**kwargs):
    return {
        'version': kwargs.get('version', settings.DEFAULT_JQUERY)
    }


@register.inclusion_tag('emarcs/lib/js/modernizr.html')
def modernizr(**kwargs):
    return {
        'version': kwargs.get('version', settings.DEFAULT_MODERNIZR)
    }


@register.inclusion_tag('emarcs/lib/js/mootools.html')
def mootools(**kwargs):
    return {
        'version': kwargs.get('version', settings.DEFAULT_MOOTOOLS)
    }


@register.inclusion_tag('emarcs/lib/js/ie8_html5.html')
def ie8_html5shiv(**kwargs):
    return {
        'version': kwargs.get('version', settings.DEFAULT_HTML5SHIV)
    }