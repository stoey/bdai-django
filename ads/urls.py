from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
    url(r'^view/(?P<pk>\d+)$', 'ads.views.view', name='ad_view'),
    url(r'^click/(?P<pk>\d+)$', 'ads.views.click', name='ad_click'),
)
