from django.db import models
from pages.models import Page

class FooterLink(object):
    def __init__(self, text, href, children=None):
        self.text = text
        self.href = href
        self.children = children

    @classmethod
    def all(cls):
        pages = Page.objects.filter(footer_link=True)
        directories = pages.values('directory', 'pk')
