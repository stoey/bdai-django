from django.db.models import F
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from .models import Advert

def click(request, pk):
    ad = get_object_or_404(Advert, pk=pk)
    ad.clicks = F('clicks') + 1
    ad.save()
    return redirect(ad.link)

def view(request, pk):
    ad = get_object_or_404(Advert, pk=pk)
    ad.impressions = F('impressions') + 1
    ad.save()
    return redirect(ad.image.url)
