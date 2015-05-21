# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to=b'images/ads/%Y/')),
                ('href', models.URLField(max_length=255)),
                ('running', models.BooleanField(default=True)),
                ('impressions', models.IntegerField()),
                ('clicks', models.IntegerField()),
            ],
        ),
    ]
