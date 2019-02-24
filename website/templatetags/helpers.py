import datetime
import re
from django import template
from django.db.models import Q
from django.urls import NoReverseMatch, reverse

from website.models import Event, Announcement, NewsMention

"""
Most of these are needed simply because of a lack of DB context within the Homepage template
"""

register = template.Library()


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
def get_current_events():
    today = datetime.datetime.today()
    return Event.objects.filter(Q(end_date__gte=today))


@register.simple_tag
def get_past_events():
    today = datetime.datetime.today()
    return Event.objects.filter(Q(end_date__lt=today))


@register.simple_tag
def get_some_current_events():
    return get_current_events()[:2]


@register.simple_tag
def get_latest_announcement():
    return Announcement.objects.order_by('-created').first()


@register.simple_tag
def get_latest_newsroom_entries():
    return NewsMention.objects.order_by('-date')[:2]
