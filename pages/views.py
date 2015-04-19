from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import render
from django.template import Template
from django.template import RequestContext
from django.template.loader import get_template

from .models import Page

def view_page(request, path):
    try:
        page = Page.from_path(path)
        content_template = get_template('page.html')
        content = content_template.render(dict(
            page=page,
        ), request)
        editlink = None
        if request.user.is_staff:
            editlink = reverse('admin:pages_page_change', args=(page.pk,))
        return render(
            request,
            page.directory.theme.template,
            dict(
                title=page.title,
                content=content,
                editlink=editlink
            ),
        )
    except Page.DoesNotExist:
        raise Http404
