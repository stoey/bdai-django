from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/event/%Y/')

    def __unicode__(self):
        return self.name


    @property
    def time(self):
        if self.start.date() == self.end.date(): # 1 day
            format_str = "{self.start:%B %d %i:%m%p}-{self.end:%i:%m%p}"
        elif self.start.month == self.end.month:
            format_str = "{self.start:%B %d}-{self.end:%d}"
        else:
            format_str = "{self.start:%B %d}-{self.end:%d}"
        return format_str.format(self=self)

class EventAction(models.Model):
    event = models.ForeignKey(Event, related_name='actions')
    name = models.CharField(max_length=100)
    link = models.URLField(blank=True, max_length=255)
    download = models.FileField(blank=True, upload_to='documents/event/%Y/')

    def __unicode__(self):
        return u"{0}: {1}".format(self.event.name, self.name)

    @property
    def href(self):
        return self.link if self.link else self.download.url
