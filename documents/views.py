from datetime import datetime

from django.core.urlresolvers import reverse
from django.shortcuts import render

from .models import Newsletter

def list_newsletters(request):
    editlink = None
    if request.user.is_staff:
        editlink = reverse('admin:documents_newsletter_changelist')
    return render(request, 'newsletters.html', dict(
        title='FactorNet Newsletters',
        newsletters=Newsletter.objects.filter(date_published__lt=datetime.now()).order_by('-date_published'),
        editlink=editlink,
    ))
