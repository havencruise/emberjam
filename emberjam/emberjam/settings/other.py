import os
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
}

APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../'))

NODE_ROOT = os.path.join(APP_ROOT, 'env', 'node_modules')
HANDLEBARS_PATH = os.path.join(NODE_ROOT, 'django-ember-precompile', 'bin', 'django-ember-precompile')
COMPRESS_PRECOMPILERS = (
    ('text/x-handlebars', '{} {{infile}}'.format(HANDLEBARS_PATH)),
)
COMPRESS_ENABLED = True