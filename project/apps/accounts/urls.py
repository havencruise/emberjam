from django.conf.urls import patterns, url, include
# from accounts import views

urlpatterns = patterns('accounts.views',
    url(r'^auth/$', 'api_auth'),
    (r'^user/', include('django.contrib.auth.urls')),
)