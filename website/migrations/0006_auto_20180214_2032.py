# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-15 03:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_event_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='After this date/time the event will move to the "Archived" section', verbose_name='expiration date'),
        ),
    ]
