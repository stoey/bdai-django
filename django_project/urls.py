from django.conf.urls import patterns, include, url
from django.conf import settings

if settings.SERVER_MODE == "admin":
    from django.contrib import admin
    admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'homepage.views.home', name='home'),
    url(r'^documents/', include('documents.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^publish/', include('publish.urls')),
    url(r'^sponsors/', include('sponsors.urls')),
)

if settings.SERVER_MODE == "admin":
    urlpatterns += patterns('',
        url(r'^admin/', include(admin.site.urls)),
        url(r'^tinymce/', include('tinymce.urls')),
    )

urlpatterns += patterns('',
    url(r'^(?P<path>.*)$', 'pages.views.view_page', name='page'),
)

