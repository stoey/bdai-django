from django.conf import settings
import os
from subprocess import check_call
import sys
from tempfile import NamedTemporaryFile

def manage_command(*args):
    return [sys.executable, sys.argv[0]] + list(args)

def should_copy(app):
    return not app.startswith('django.') and app not in ('publish', 'tinymce')

APPS = [a for a in settings.INSTALLED_APPS if should_copy(a)]

def dumpdata(filename, server_mode='admin'):
    with open(filename, 'w') as f:
        kwargs = dict(
            args=manage_command('dumpdata', *APPS),
            env=dict(SERVER_MODE=server_mode),
            stdout=f,
        )
        check_call(**kwargs)


def loaddata(filename, server_mode='live'):
    with open(filename) as f:
        kwargs = dict(
            args=manage_command('loaddata'),
            env=dict(SERVER_MODE=server_mode),
            stdin=f,
        )
        check_call(**kwargs)


def publish():
    with NamedTemporaryFile as f:
        dumpdata(f.name)
        loaddata(f.name)


def test():
    return True
