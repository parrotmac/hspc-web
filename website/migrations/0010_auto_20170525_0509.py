# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 05:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20170525_0444'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['hidden_date']},
        ),
        migrations.AddField(
            model_name='infopage',
            name='page_title',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]