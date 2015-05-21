from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'homepage.views.home', name='home'),
    url(r'^ads/', include('ads.urls')),
    url(r'^documents/', include('documents.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^sponsors/', include('sponsors.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^(?P<path>.*)$', 'pages.views.view_page', name='page'),
)

