from django.core.urlresolvers import reverse
from django.shortcuts import render

from .models import Sponsor

def list_sponsors(request):
    editlink = None
    if request.user.is_staff:
        editlink = reverse('admin:sponsors_sponsor_changelist')


    return render(request, 'sponsors.html', dict(
        title='Sponsors',
        sponsors=Sponsor.objects.order_by('name'),
        editlink=editlink,
    ))
