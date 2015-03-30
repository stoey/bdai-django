from django.http import Http404
from django.shortcuts import render
from django.template import Template
from django.template import RequestContext

from .models import Page

def view_page(request, path):
    try:
        page = Page.from_path(path)
        return render(
            request,
            page.directory.theme.template,
            dict(
                title=page.title,
                content=page.contents,
            ),
        )
    except Page.DoesNotExist:
        raise Http404
