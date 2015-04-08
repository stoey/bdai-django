from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import render
from django.template import Template
from django.template import RequestContext

from .models import Page

def view_page(request, path):
    try:
        page = Page.from_path(path)
        editlink = None
        if request.user.is_staff:
            editlink = reverse('admin:pages_page_change', args=(page.pk,))
        return render(
            request,
            page.directory.theme.template,
            dict(
                title=page.title,
                content=page.contents,
                editlink=editlink
            ),
        )
    except Page.DoesNotExist:
        raise Http404
