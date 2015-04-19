# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('expires', models.DateField()),
                ('background_image', models.ImageField(upload_to=b'images/banner/%Y/')),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BannerAction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('link', models.URLField(max_length=255, blank=True)),
                ('download', models.FileField(upload_to=b'documants/banner/%Y/', blank=True)),
                ('banner', models.ForeignKey(related_name=b'actions', to='homepage.Banner')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TextBox',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100, choices=[(b'about_bdai', b'About BDAI'), (b'partner_council', b'BDAI Partner Council'), (b'newly_diagnosed', b'Newly Diagnosed?')])),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Text boxes',
            },
            bases=(models.Model,),
        ),
    ]
