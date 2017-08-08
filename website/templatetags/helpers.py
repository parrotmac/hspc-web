import datetime
import re
from django import template
from django.db.models import Q
from django.urls import NoReverseMatch, reverse

from website.models import MenuEntry, Event, EventCategory

register = template.Library()

@register.simple_tag
def get_main_navigation():
    menu_entries = MenuEntry.objects.all()
    return menu_entries

@register.simple_tag(takes_context=True)
def active(context, pattern_or_urlname):
    try:
        pattern = '^' + reverse(pattern_or_urlname) + '$'
    except NoReverseMatch:
        pattern = pattern_or_urlname
    path = context['request'].path
    if re.search(pattern, path):
        return 'active'
    return ''

@register.simple_tag
def get_future_events():
    today = datetime.datetime.today()
    return Event.objects.filter(Q(hidden_date__gte=today))

@register.simple_tag
def get_past_events():
    today = datetime.datetime.today()
    return Event.objects.filter(Q(hidden_date__lt=today))

@register.simple_tag
def get_upcoming_events():
    return Event.objects.order_by("hidden_date")[:3]
