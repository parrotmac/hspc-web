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


class ExposedMetadataModel(models.Model):

    def get_verbose_name(self):
        return self._meta.verbose_name

    def get_verbose_name_plural(self):
        return self._meta.verbose_name_plural

    def get_api_base_url(self):
        return "/api/v1/{}/".format(self._meta.model_name)

    class Meta:
        abstract = True


class EventCategory(ExposedMetadataModel):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "event categories"


class Event(ExposedMetadataModel):
    category = models.ForeignKey(EventCategory, null=True)
    title = models.CharField(max_length=128)
    hidden_date = models.DateTimeField(default=datetime.now, help_text='Used to sort events', verbose_name='sortable date')
    display_date = models.CharField(max_length=128, help_text="Text shown such as 'Feb 4th - 8th' or 'March 25'")
    location = models.CharField(max_length=128)
    event_details = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["hidden_date"]



class RegistrationRequest(models.Model):
    full_name = models.CharField(max_length=256)
    title = models.CharField(max_length=256, blank=True, null=True)
    organization_name = models.CharField(max_length=256, blank=True, null=True)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=64)
    comments = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        sane_full_name = self.full_name.strip()

        if self.title is None:
            return sane_full_name
        else:
            return "{} ({})".format(sane_full_name, self.title)


class MenuEntry(models.Model):
    '''
    This model will likely be removed in the future
    '''
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



'''
# # # # # # # # # # # # # # # # # # # #
# # #  Begin Wagtail-based models # # #
# # # # # # # # # # # # # # # # # # # #
'''

class HomePage(MenuPage):
    body = RichTextField(blank=True)

    membership_text = RichTextField(blank=True)
    collaboration_text = RichTextField(blank=True)
    marketplace_text = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel('membership_text'),
        FieldPanel('collaboration_text'),
        FieldPanel('marketplace_text'),
    ]


class InfoPage(MenuPage):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]


class RobustInfoPage(Page):
    author = models.CharField(max_length=255)
    date = models.DateField("Last updated")
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('separator', blocks.StaticBlock()),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])

    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('date'),
        StreamFieldPanel('body'),
    ]

'''
# # # # # # # # # # # # # # # # # # # #
# # #  End Wagtail-based models # # #
# # # # # # # # # # # # # # # # # # # #
'''