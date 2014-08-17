import os
SITE_NAME = os.environ['DJANGO_SITE_NAME']

if not SITE_NAME:
    raise EnvironmentError, 'DJANGO_SITE_NAME not found in environment'

COMPRESS_JS = {
    'framework': {
        'source_filenames': (

        ),
        'output_filename': '%s/js/framework.r?.js' % SITE_NAME
    },
}
PIPELINE_JS = COMPRESS_JS

COMPRESS_CSS = {
    'framework': {
        'source_filenames': (

         ),
        'output_filename': '%s/css/framework.r?.css' % SITE_NAME
    },
}
PIPELINE_CSS = COMPRESS_CSS
