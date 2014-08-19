from django.conf.urls import patterns, url
# from accounts import views

urlpatterns = patterns('accounts.views',
    url(r'^auth/$', 'api_auth'),
)