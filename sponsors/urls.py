from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
    url(r'^$', 'sponsors.views.list_sponsors', name='sponsors_list'),
)
