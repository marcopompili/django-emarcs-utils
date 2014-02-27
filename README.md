django-emarcs-utils
===================

Some models and other utils to semplify developing with Django.


Installation
------------
This application is still not published as a package, but you can clone the repository and do a local installation with pip like this:
```bash
pip install -e django-emarcs-utils
```

Configuration
-------------
The configuration is pretty basic just add these lines to your settings.py file:
```python

import django.conf.global_settings as DEFAULT_SETTINGS

# [...]

INSTALLED_APPS = (
...
'emarcs'
...
)


TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    'emarcs.processors.on_debug',
)

```

The template processor check the DEBUG constant of settings.py, in case of DEBUG = True, the non minimized sources of the libraries are loaded, in case of DEBUG = False, the production versions of the libraries will be used.


Use it
------
To use the libraries on a template it's simple, just use the include template tag of django:
```
# To include jquery
{% include "emarcs/lib/js/jquery.html" %}
```

Libraries
------------
The list of the libraries that you can include.
* jquery 1.11.0
* jquery 2.1.0
* Bootstrap 3.1.1
* Font Awesome 4.0.3
* IE8 HTML5Shiv
