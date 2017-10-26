# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 18:37
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20171023_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('homepage_panel', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('material_icon_name', wagtail.wagtailcore.blocks.CharBlock()), ('body', wagtail.wagtailcore.blocks.TextBlock()), ('link_url', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('link_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('link_is_external', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), ('background_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('overlay_css_background_color', wagtail.wagtailcore.blocks.CharBlock())))),), blank=True),
        ),
    ]
