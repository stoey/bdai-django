from django.contrib import admin

from .models import Advert

class AdvertAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'running',
        'impressions',
        'clicks',
    ]
    readonly_fields = ('impressions', 'clicks')

admin.site.register(Advert, AdvertAdmin)
