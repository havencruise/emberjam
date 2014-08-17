import os
APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../'))

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"

MEDIA_ROOT = APP_ROOT + '/media/upload'
STATIC_ROOT = APP_ROOT + '/resources'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/upload/'
STATIC_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

PIPELINE = True
PIPELINE_VERSION = True
PIPELINE_VERSION_REMOVED_OLD = True
PIPELINE_CSS_COMPRESSOR = ()
PIPELINE_JS_COMPRESSOR = ()


#PIPELINE SETTINGS ARE IN <site_name>.settings.media file