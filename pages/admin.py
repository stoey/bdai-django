from django.contrib import admin
from django.db.models import TextField

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

admin.site.register(Page, PageAdmin)

