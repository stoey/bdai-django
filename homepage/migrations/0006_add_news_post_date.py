# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_add_news_action_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsitem',
            name='post_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 19, 22, 49, 7, 749461)),
            preserve_default=False,
        ),
    ]
