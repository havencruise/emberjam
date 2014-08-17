import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('Prashanth', 'sinewpod@gmail.com'),
)

MANAGERS = ADMINS

SITE_NAME = os.environ['DJANGO_SITE_NAME']

#MIDDLEWARE_CLASSES should in <site_name>.settings.app.py file
#INSTALLED_APPS should be in <site_name>.settings.app.py file

ROOT_URLCONF = SITE_NAME + '.urls'

CACHE_BACKEND = 'memcached://127.0.0.1:11211/?timeout=3600'




