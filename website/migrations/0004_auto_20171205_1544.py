# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-05 22:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20171023_1237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='robustinfopage',
            name='author',
        ),
        migrations.RemoveField(
            model_name='robustinfopage',
            name='date',
        ),
    ]