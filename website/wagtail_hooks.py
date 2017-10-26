from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from wagtail.wagtailcore.fields import RichTextField

from .models import Event, EventCategory, Announcement, NewsMention


class EventModelAdmin(ModelAdmin):
    model = Event
    # menu_label = 'Events'  # ditch this to use verbose_name_plural from model
    menu_icon = 'date'  # change as required
    menu_order = 230  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = (
        'title',
        'display_date',
        'hidden_date',
        'category',
        'location',
        'event_details',
    )
    list_filter = ('title', 'hidden_date', 'location',)
    search_fields = ('title', 'display_date',)


class EventCategoryAdmin(ModelAdmin):
    model = EventCategory
    menu_icon = 'date'  # change as required
    menu_order = 220  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = (
        'name',
    )
    list_filter = ('name',)
    search_fields = ('name',)


class AnnouncementAdmin(ModelAdmin):
    model = Announcement
    menu_icon = 'pick'
    menu_order = 240
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = (
        'hidden_label',
        'created',
        'announcement',
    )
    list_filter = (
        'hidden_label',
        'created',
    )
    search_fields = (
        'hidden_label',
        'created',
        'announcement',
    )

class NewsAdmin(ModelAdmin):
    model = NewsMention
    menu_icon = 'doc-full-inverse'
    menu_order = 250
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = (
        'source',
        'date',
        'article_title',
        'url',
    )
    list_filter = (
        'source',
        'date',
        'article_title',
        'url',
    )
    search_fields = (
        'source',
        'date',
        'article_title',
        'url',
    )


# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(EventModelAdmin)
modeladmin_register(EventCategoryAdmin)
modeladmin_register(AnnouncementAdmin)
modeladmin_register(NewsAdmin)
