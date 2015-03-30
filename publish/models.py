from django.conf import settings
from django.db import models
from os.path import join

from publish.commands import dumpdata

class Snapshot(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    @property
    def path(self):
        if None in (self.pk, self.timestamp):
            return None
        timestamp = self.timestamp.strftime("%Y%m%d-%H%M%S")
        name = 'snapshot-{self.pk}-{timestamp}.json'.format(
            self=self,
            timestamp=timestamp,
        )
        return join(settings.SNAPSHOTS_PATH,name)

    @classmethod
    def create(cls):
        snapshot = cls()
        snapshot.save()
        dumpdata(snapshot.path, settings.SERVER_MODE)
        snapshot.complete = True
        snapshot.save()
        return snapshot
