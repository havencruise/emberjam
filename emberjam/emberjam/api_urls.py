from django.conf.urls import url, patterns, include

urlpatterns = patterns('snippets.views',
    url(r'^user/', include('accounts.api_urls')),
)