# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Directory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('parent', models.ForeignKey(related_name=b'subdirectories', blank=True, to='pages.Directory', null=True)),
            ],
            options={
                'verbose_name_plural': 'Directories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, blank=True)),
                ('title', models.CharField(max_length=100)),
                ('contents', models.TextField()),
                ('footer_link', models.BooleanField(default=False, help_text=b'Should this page appear in the footer?')),
                ('directory', models.ForeignKey(related_name=b'pages', to='pages.Directory')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('template', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='page',
            unique_together=set([('name', 'directory')]),
        ),
        migrations.AddField(
            model_name='directory',
            name='theme',
            field=models.ForeignKey(default=1, to='pages.Theme'),
            preserve_default=True,
        ),
    ]
