from django import template
from django.template.loader import get_template

from ads.models import Advert

register = template.Library()

@register.simple_tag
def display_ad():
    advert = Advert.random()
    if advert is not None:
        template = get_template('display_ad.html')
        advert.save()
        return template.render(dict(ad=advert))
