# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_add_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsitem',
            name='download',
            field=models.FileField(upload_to=b'documents/news/%Y/', blank=True),
        ),
        migrations.AddField(
            model_name='newsitem',
            name='link',
            field=models.URLField(max_length=255, blank=True),
        ),
    ]
