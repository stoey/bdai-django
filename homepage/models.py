from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=200)
    expires = models.DateField()
    background_image = models.ImageField(upload_to='images/banner/%Y/')
    description = models.TextField()

    def __unicode__(self):
        return self.title

class BannerAction(models.Model):
    banner = models.ForeignKey('Banner', related_name='actions')
    name = models.CharField(max_length=100)
    link = models.URLField(blank=True, max_length=255)
    download = models.FileField(blank=True, upload_to='documants/banner/%Y/')

    def __unicode__(self):
        return u"{0}: {1}".format(self.banner.title, self.name)

    @property
    def href(self):
        return self.link if self.link else self.download.url

class TextBox(models.Model):
    TITLES = dict(
        newly_diagnosed='Newly Diagnosed?',
        about_bdai='About BDAI',
        partner_council='BDAI Partner Council',
    )
    name = models.CharField(max_length=100, choices=TITLES.items(), unique=True)
    text = models.TextField()

    class Meta:
        verbose_name_plural = 'Text boxes'

    def __unicode__(self):
        return self.get_name_display()
