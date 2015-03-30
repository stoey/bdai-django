from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
    url(r'^(?P<id>\d+)/(?P<name>.*)', 'documents.views.document', name='document_view'),
)
