from django.contrib import admin
from django.db.models import TextField
from django.conf.urls import patterns, url

from tinymce.widgets import TinyMCE

from .models import Page
from .models import Theme

class PageAdmin(admin.ModelAdmin):
    list_display = [
        'path',
        'title',
        'name',
        'directory',
        'footer_link',
    ]
    ordering = (
        'directory',
        'name',
    )
    formfield_overrides = {
        TextField: dict(widget=TinyMCE(attrs=dict(cols=80, rows=30, style="width: 100%")))
    }

    def get_urls(self):
        urls = super(PageAdmin, self).get_urls()
        extra_urls =  patterns('',
            url(r'^todo/$', 'pages.admin_views.todo', name='admin_pages_todo')
        )
        return extra_urls + urls

admin.site.register(Page, PageAdmin)


