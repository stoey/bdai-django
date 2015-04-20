# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_add_news_actions'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsItemAction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.URLField(max_length=255, blank=True)),
                ('download', models.FileField(upload_to=b'documents/news/%Y/', blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='newsitem',
            name='download',
        ),
        migrations.RemoveField(
            model_name='newsitem',
            name='link',
        ),
        migrations.AddField(
            model_name='newsitemaction',
            name='news_item',
            field=models.ForeignKey(related_name='actions', to='homepage.NewsItem'),
        ),
    ]
