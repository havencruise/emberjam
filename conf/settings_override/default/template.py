# -*- coding: utf-8 -*-
import os
APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../'))

SITE_NAME = os.environ['DJANGO_SITE_NAME']

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    )


TEMPLATE_DIRS = (
    APP_ROOT + '/' + SITE_NAME + '/' + SITE_NAME + '/templates',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request"
)
