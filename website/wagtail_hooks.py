from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import Event, EventCategory


class EventModelAdmin(ModelAdmin):
    model = Event
    # menu_label = 'Events'  # ditch this to use verbose_name_plural from model
    menu_icon = 'date'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
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
    menu_order = 300  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = (
        'name',
    )
    list_filter = ('name',)
    search_fields = ('name',)


# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(EventModelAdmin)
modeladmin_register(EventCategoryAdmin)
