from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
    url(r'^$', 'events.views.list_events', name='events_list'),
)
