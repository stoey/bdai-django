from django.contrib import admin

from .models import Banner
from .models import BannerAction
from .models import TextBox

class BannerActionAdmin(admin.TabularInline):
    model = BannerAction

class BannerAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'expires',
    )
    date_hierarchy = 'expires'
    ordering = (
        '-expires',
    )
    search_fields = (
        'title',
        'description',
    )
    inlines = [
        BannerActionAdmin,
    ]

class TextBoxAdmin(admin.ModelAdmin):
    pass

admin.site.register(Banner, BannerAdmin)
admin.site.register(TextBox, TextBoxAdmin)
