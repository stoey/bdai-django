from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
     url(r'^newsletters', 'documents.views.list_newsletters', name='newsletter_list'),
)
