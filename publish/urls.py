from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
    url(r'^test', 'publish.views.test', name='publish_test'),
    url(r'^publish', 'publish.views.publish', name='publish_publish'),
)
