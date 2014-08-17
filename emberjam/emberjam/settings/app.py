
SITE_ID = 1 # you should change this if its multi site

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'core.middleware.BaseTemplateSetter'
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django_extensions',
    'south',
    'pipeline',
    'core'
)

SECRET_KEY = '2y%jux-*3x6-w!x7+4zl_fybxv)306r&@mu^r8@$xbzopqgg7u'
