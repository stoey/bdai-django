from datetime import datetime

from django.core.urlresolvers import reverse
from django.shortcuts import render

from .models import Event

def list_events(request):
    editlink = None
    if request.user.is_staff:
        editlink = reverse('admin:events_event_changelist')

    return render(request, 'events.html', dict(
        title="Upcoming Events",
        events=Event.objects.filter(end__gt=datetime.now()).order_by('start'),
        editlink=editlink,
    ))
