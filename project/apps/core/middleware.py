#http://code.djangoproject.com/wiki/CookBookThreadlocalsAndUser
# threadlocals middleware, use at your own risk
try:
    from threading import local
except ImportError:
    from django.utils._threading_local import local

_thread_locals = local()

def get_current_user():
    return getattr(_thread_locals, 'user', None)

def get_current_session():
    return getattr(_thread_locals, 'session', None)

class ThreadLocals(object):
    """Middleware that gets various objects from the
    request object and saves them in thread local storage."""
    def process_request(self, request):
        _thread_locals.user = getattr(request, 'user', None)
        _thread_locals.session = getattr(request, 'session', None)



import re
from django.conf import settings

class BaseTemplateSetter(object):
    def process_request(self, request):
        if not hasattr(request, 'base_template'):
            setattr(request, 'base_template', 'base.html')


class DeviceTemplateDetect(object):
    """
    Middleware to detect if an alternate device is being used.

    If detected, it uses settings.DEVICE_TEMPLATE_ROUTING to inject the name
    provided in the configuration of the template before being passed to the
    loader to see if the template exists.

    To be used with renderutils.render_to

    e.g.
    settings.DEVICE_TEMPLATE_ROUTING = (
        ("P<key>iPhone|iPad|iPod|$", "ios"),
        ("P<key>Android|$", "android"),
      )

    will look at HTTP_USER_AGENT and if it matches on ios,
    then from a view if one is trying to load 'accounts/login.html'
    the render_to will turn that into (accounts/login.ios.html, account/login.html)
    to be sent to the loader to see the first template matches so that you can
    provide device specific templates.

    If no routing is specified, the default routing is:
      (?P<key>iPhone|iPad|Android|iPod|IEMobile|BlackBerry|Mobile\sSafari|$)", "mobile", "base.mobile.html", "is_mobile")

    """


    DEFAULT_ROUTING = ((
        "(?P<key>iPhone|iPad|Android|iPod|IEMobile|BlackBerry|Mobile\sSafari|$)", 
            "mobile", 
            "base.mobile.html", 
            "is_mobile"),
    )

    DEFAULT_SETTINGS = getattr(settings, 'DEVICE_TEMPLATE_ROUTING', DEFAULT_ROUTING)

    def process_request(self, request):
        agent = request.META.get('HTTP_USER_AGENT', '')
        for row in self.DEFAULT_SETTINGS:
            if len(row) > 1:
                if len(re.findall(row[0], agent)) > 1:
                    setattr(request, '_use_alternate_template', row[1])
                    if len(row) > 2:
                        setattr(request, 'base_template', row[2])
                    if len(row) > 3:
                        setattr(request, row[3], True)
                    break

