import os
SITE_NAME = os.environ['DJANGO_SITE_NAME']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'verbose': {
            'format': '[%(levelname)s] {%(asctime)s %(module)s.%(funcName)s() @%(filename)s:%(lineno)d %(process)d %(thread)d}: %(message)s'
        },
        'simple': {
            'format': '[%(levelname)s] {%(asctime)s}: %(message)s'
        },
    },

    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file': {
            'level': 'INFO',
            'class': 'cloghandler.ConcurrentRotatingFileHandler',
            'filename': '/tmp/'+ SITE_NAME +'.log',
            'maxBytes': 10*1024*1024,
            'backupCount': 5,
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
            'formatter': 'verbose',
        }
    },

    'loggers': {
        # 'django': {
        #     'handlers':['console', 'mail_admins'],
        #     'propagate': True,
        #     'level':'ERROR',
        # },
        'django': {
            'handlers':['console'],
            'propagate': True,
            'level':'INFO',
        },
    }
}
