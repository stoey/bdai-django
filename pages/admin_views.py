from django.shortcuts import render

from .models import Page

def todo(request):
    pages = Page.objects.filter(contents="") 
    return render(
        request,
        'admin/todo.html',
        dict(
            title="TODO Pages",
            pages=pages
        ),
    )
