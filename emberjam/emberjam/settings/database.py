#this should probably be in the environment files and not here

import os
SQLITE_PATH = os.path.abspath(os.path.join(
                os.path.dirname(os.path.abspath(__file__)), 
                '../db.sqlite3'))

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.sqlite3',# Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
       'NAME': '%s' % SQLITE_PATH,            # Or path to database file if using sqlite3.
       'USER': '',                            # Not used with sqlite3.
       'PASSWORD': '',                        # Not used with sqlite3.
       'HOST': '',                            # Set to empty string for localhost. Not used with sqlite3.
       'PORT': '',                            # Set to empty string for default. Not used with sqlite3.
   }
}
