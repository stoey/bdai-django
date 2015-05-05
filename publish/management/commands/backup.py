from bz2 import BZ2File
from datetime import datetime
from hashlib import sha1
from os import makedirs
from os import link
from os import symlink
from os import walk
from os.path import dirname
from os.path import exists
from os.path import join
from os.path import realpath
from StringIO import StringIO

from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management import call_command

INDEX_FORMAT = "{0:%Y}/{0:%m}/{0:%d}/{0:%H}:{0:%M}/data.json.bz2"

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '-o',
            '--output-dir',
            dest='output_dir',
            help='Output directory',
        )

    def handle(self, *args, **options):
        output_dir = options.get('output_dir')
        data_f = StringIO()
        call_command(
            'dumpdata',
            all=True,
            indent=2,
            stdout=data_f
        )

        json_data = data_f.getvalue()
        data_hash = sha1(json_data).hexdigest()
        filename = "{path}/{hash}.json.bz2".format(
            path=output_dir,
            hash=data_hash
        )
        with BZ2File(filename, 'w') as f:
            f.write(json_data)

        index_path = join(output_dir, 'index')
        index_filepath = join(
            index_path,
            INDEX_FORMAT.format(datetime.now())
        )
        index_dir = dirname(index_filepath)
        if not exists(index_dir):
            makedirs(index_dir)
        symlink(filename, index_filepath)
        index_files_path = join(index_dir, 'files')
        if not exists(index_files_path):
            makedirs(index_files_path)
        uploads_path = settings.MEDIA_ROOT
        for path, dirs, files in walk(uploads_path):
            prefix = path[len(uploads_path):]
            dest_path = index_files_path + prefix
            if not exists(dest_path):
                makedirs(dest_path)
            for f in files:
                src = join(path, f)
                dest = join(dest_path, f)
                link(src, dest)
