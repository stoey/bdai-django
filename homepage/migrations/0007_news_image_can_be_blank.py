# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_add_news_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsitem',
            name='image',
            field=models.ImageField(upload_to=b'images/news/%Y/', blank=True),
        ),
    ]
