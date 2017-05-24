from datetime import datetime

from django.contrib.flatpages.models import FlatPage
from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page
from wagtailmenus.models import MenuPage, MainMenuItem


class Event(models.Model):
    title = models.CharField(max_length=128)
    hidden_date = models.DateTimeField(default=datetime.now, help_text='Used to sort events')
    display_date = models.CharField(max_length=128, help_text="Text shown such as 'Feb 4th - 8th' or 'March 25'")
    event_location = models.CharField(max_length=128)
    event_details = models.TextField()

    def __str__(self):
        return self.title


class MenuEntry(models.Model):
    order = models.IntegerField(default=0)
    is_divider = models.BooleanField(default=False)
    top_level_name = models.CharField(
        max_length=128,
        blank=True,
        null=True,
        help_text='Only used if this is a top-level menu entry'
    )
    flat_page = models.ForeignKey(FlatPage, blank=True, null=True)
    parent = models.ForeignKey('MenuEntry', blank=True, null=True)

    def __str__(self):
        if self.flat_page is not None:
            return self.flat_page.title
        if self.top_level_name is not None:
            return self.top_level_name
        return "-" * 8

    def get_url(self):
        if self.flat_page is not None:
            return self.flat_page.get_absolute_url()
        return None

    class Meta:
        verbose_name_plural = "Menu Entries"
        ordering = ["order"]


class HomePage(MenuPage):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

class ContentPage(MainMenuItem):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]
