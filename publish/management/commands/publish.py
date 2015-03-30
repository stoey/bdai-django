from django.conf import settings
from django.core.management.base import CommandError
from django.core.management.base import NoArgsCommand

from publish import commands
class Command(NoArgsCommand):
    def handle_noargs(self):
        mode = settings.SERVER_MODE
        if mode != 'admin':
            raise CommandError("Must be run in admin mode")
        commands.publish()

