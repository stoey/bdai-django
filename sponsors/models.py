from django.db import models

class Sponsor(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(upload_to='images/sponsors')
    url = models.URLField(max_length=255)

    def __unicode__(self):
        return self.name
