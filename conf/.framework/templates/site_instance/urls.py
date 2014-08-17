from django.conf.urls import patterns, include
from django.contrib import admin
from core.utils.renderutils import render_to

admin.autodiscover()

@render_to('index.html')
def default_view(request):
    return {}

urlpatterns = patterns('',
    (r'^$', 'urls.default_view'),
    (r'^__admin__/', include(admin.site.urls)),
)