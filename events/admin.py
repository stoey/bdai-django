from django.contrib import admin

from .models import Event
from .models import EventAction

class EventActionAdmin(admin.TabularInline):
    model = EventAction

class EventAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'start',
        'end',
    )
    date_hierarchy = 'start'
    ordering = (
        '-start',
        '-end',
    )
    search_fields = (
        'name',
        'description',
    )
    inlines = [
        EventActionAdmin,
    ]

admin.site.register(Event, EventAdmin)
