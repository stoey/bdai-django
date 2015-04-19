# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to=b'images/event/%Y/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventAction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('link', models.URLField(max_length=255, blank=True)),
                ('download', models.FileField(upload_to=b'documents/event/%Y/', blank=True)),
                ('event', models.ForeignKey(related_name=b'actions', to='events.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
