from datetime import datetime

from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import render_to_string

from events.models import Event
from homepage.models import Banner
from homepage.models import TextBox
from sponsors.models import Sponsor

def home(request):
    now = datetime.now()
    context = dict(
        banner=Banner.objects.filter(expires__gt=now).order_by('-expires')[0],
        event=Event.objects.filter(end__gt=now).order_by('start')[0],
        sponsors=Sponsor.objects.order_by('?'),
        text_boxes=dict([(b.name, b) for b in TextBox.objects.all()]),
    )
    return render(request, 'home.html', context)
