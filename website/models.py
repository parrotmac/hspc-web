from datetime import datetime

from django.db import models
from django.contrib.flatpages.models import FlatPage
from wagtailmenus.models import MenuPage, MainMenuItem
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock

from website.blocks import HomepagePanelBlock


class EventCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "event categories"


class Event(models.Model):
    category = models.ForeignKey(EventCategory, null=True)
    title = models.CharField(max_length=128)
    hidden_date = models.DateTimeField(default=datetime.now, help_text='Used to sort events', verbose_name='sortable date')
    display_date = models.CharField(max_length=128, help_text="Text shown such as 'Feb 4th - 8th' or 'March 25'")
    location = models.CharField(max_length=128)
    event_details = RichTextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["hidden_date"]


class Announcement(models.Model):
    hidden_label = models.CharField(max_length=255, help_text='Only displayed in the CMS or Admin UI.')
    created = models.DateTimeField(default=datetime.now, editable=False)
    announcement = RichTextField()

    def __str__(self):
        return self.hidden_label


class NewsMention(models.Model):
    source = models.CharField(max_length=255)
    date = models.DateField()
    url = models.URLField()
    article_title = models.CharField(max_length=255)

    def __str__(self):
        return "{} - {}".format(self.source, self.date)


class RegistrationRequest(models.Model):
    full_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    organization_name = models.CharField(max_length=255, blank=True, null=True)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=64)
    comments = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        sane_full_name = self.full_name.strip()

        if self.title is None or self.title.strip() == "":
            return sane_full_name
        else:
            return "{} ({})".format(sane_full_name, self.title)



'''
# # # # # # # # # # # # # # # # # # # #
# # #  Begin Wagtail-based models # # #
# # # # # # # # # # # # # # # # # # # #
'''

class HomePage(MenuPage):

    body = StreamField([
        ('homepage_panel', HomepagePanelBlock()),
    ], blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]


class BasicInfoPage(MenuPage):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]


class RobustInfoPage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('separator', blocks.StaticBlock()),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

'''
# # # # # # # # # # # # # # # # # # # #
# # #  End Wagtail-based models # # #
# # # # # # # # # # # # # # # # # # # #
'''