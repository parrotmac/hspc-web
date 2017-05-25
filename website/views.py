from django.shortcuts import render
from django.views.generic import ListView

from website.models import Event, EventCategory


class EventListView(ListView):

    model = EventCategory
    template_name = "website/events.html"

    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)
        return context
