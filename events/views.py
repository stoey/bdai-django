from datetime import datetime

from django.shortcuts import render

from .models import Event

def list_events(request):
    return render(request, 'events.html', dict(
        title="Upcoming Events",
        events=Event.objects.filter(end__gt=datetime.now()).order_by('start'),
    ))
