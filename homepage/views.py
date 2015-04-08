from datetime import datetime

from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import render_to_string

from events.models import Event
from homepage.models import Banner
from homepage.models import TextBox
from sponsors.models import Sponsor

def home(request):
    now = datetime.now()
    banners = Banner.objects.filter(expires__gt=now).order_by('-expires')
    events = Event.objects.filter(end__gt=now).order_by('start')
    editlink = None
    if request.user.is_staff:
        editlink = reverse('admin:app_list', args=('homepage', ))

    context = dict(
        title='Home',
        banner= banners[0] if banners.count() else None,
        event=events[0] if events.count() else None,
        sponsors=Sponsor.objects.order_by('?'),
        text_boxes=dict([(b.name, b) for b in TextBox.objects.all()]),
        editlink=editlink,
    )
    return render(request, 'home.html', context)
