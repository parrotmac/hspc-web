# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 01:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flatpages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('hidden_date', models.DateTimeField(default=datetime.datetime.now, help_text='Used to sort events')),
                ('display_date', models.CharField(help_text="Text shown such as 'Feb 4th - 8th' or 'March 25'", max_length=128)),
                ('event_location', models.CharField(max_length=128)),
                ('event_details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MenuEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('flat_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='flatpages.FlatPage')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.MenuEntry')),
            ],
        ),
    ]
