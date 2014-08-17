import os, sys

filepath = os.path.abspath(__file__)
environment = os.path.dirname(filepath).split('/')[-1]
sitename = ".".join(filepath.split('/')[-1].split('.')[:-1])

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "%s.settings" % sitename)
os.environ['PYTHON_EGG_CACHE'] = '/tmp'
os.environ['DJANGO_SITE_NAME'] = sitename
os.environ['DJANGO_ENVIRONMENT'] =  environment

#this should be /opt/location or where on file system root directory is
#assumption is this file is in .../conf/deployment/wsgi/<env>/<site>.wsgi
deployment_location = "/".join(filepath.split('/')[:-5])

if os.path.isdir(deployment_location + '/env/lib/python2.7/site-packages'):
    import site
    site.addsitedir(deployment_location + '/env/lib/python2.7/site-packages')

sys.path += [deployment_location + '/project/apps', deployment_location + '/conf', deployment_location + sitename, deployment_location + sitename + '/' + sitename]

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
