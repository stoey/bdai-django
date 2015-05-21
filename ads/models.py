from django.db import models

class Advert(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/ads/%Y/')
    link = models.URLField(max_length=255)
    running = models.BooleanField(default=True)
    impressions = models.IntegerField(default=0)
    clicks = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


    @classmethod
    def random(cls):
        running_ads = cls.objects.filter(running=True)
        if running_ads.count() > 0:
            return running_ads.order_by('?')[0]
        else:
            return None
