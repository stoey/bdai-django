from django.contrib import admin

from .models import Document
from .models import Newsletter

class DocumentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'url',
    )
    readonly_fields = (
        'url',
    )

class NewsletterAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'date_published',
        'url',
    )
    ordering = (
        '-date_published',
    )
    readonly_fields = (
        'url',
    )

admin.site.register(Document, DocumentAdmin)
admin.site.register(Newsletter, NewsletterAdmin)
