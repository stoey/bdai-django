from django.db import models
from django.utils.timezone import localtime

class Event(models.Model):
    name = models.CharField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/event/%Y/')
    location = models.TextField(default="", blank=True)

    def __unicode__(self):
        return self.name


    @property
    def time(self):
        start = localtime(self.start)
        end = localtime(self.end)
        if start.date() == end.date(): # 1 day
            format_str = "{start:%B %d}: {start:%l:%M%p} - {end:%l:%M%p}"
        elif start.month == end.month:
            format_str = "{start:%B %d} - {end:%d}"
        else:
            format_str = "{start:%B %d} - {end:%d}"
        return format_str.format(start=start, end=end)

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
