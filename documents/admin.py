from django.contrib import admin

from .models import Document

class DocumentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'url',
    )
    readonly_fields = (
        'url',
    )

admin.site.register(Document, DocumentAdmin)
