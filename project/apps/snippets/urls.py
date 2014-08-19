from django.conf.urls import patterns, url
from snippets import views

urlpatterns = patterns('snippets.views',
    url(r'^$', views.SnippetList.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', views.SnippetDetail.as_view()),
)