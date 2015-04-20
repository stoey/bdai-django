from django.contrib import admin

from .models import Banner
from .models import BannerAction
from .models import NewsItem
from .models import NewsItemAction
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


class NewsItemActionAdmin(admin.TabularInline):
    model = NewsItemAction

class NewsItemAdmin(admin.ModelAdmin):
    ordering = (
        'post_date',
    )
    inlines = [
        NewsItemActionAdmin,
    ]
    pass

admin.site.register(Banner, BannerAdmin)
admin.site.register(TextBox, TextBoxAdmin)
admin.site.register(NewsItem, NewsItemAdmin)
