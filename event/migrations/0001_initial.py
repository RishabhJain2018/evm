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
                ('event_name', models.CharField(max_length=200)),
                ('event_description', models.CharField(max_length=200)),
                ('event_location', models.CharField(max_length=200)),
                ('event_start', models.DateTimeField()),
                ('event_end', models.DateTimeField()),
                ('event_poster', models.ImageField(upload_to=b'')),
            ],
        ),
    ]
