from django.shortcuts import render

from .models import Sponsor

def list_sponsors(request):
    return render(request, 'sponsors.html', dict(
        title='Sponsors',
        sponsors=Sponsor.objects.order_by('name'),
    ))
