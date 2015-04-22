from django.db import models

class Document(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents/%Y/')

    def __unicode__(self):
        return self.name

    @property
    def url(self):
        return self.file.url

    def get_absolute_url(self):
        return self.url

class Newsletter(models.Model):
    name = models.CharField(max_length=100)
    date_published = models.DateField()
    file = models.FileField(upload_to='documents/newsletter/%Y/')

    @property
    def url(self):
        return self.file.url

    def get_absolute_url(self):
        return self.url
