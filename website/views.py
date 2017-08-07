from django.shortcuts import render
from django.views.generic import ListView, CreateView, View

from website.forms import RegistrationRequestForm
from website.models import Event, EventCategory


class EventListView(ListView):

    model = EventCategory
    template_name = "website/events.html"

    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)
        return context

class RegistrationRequestView(CreateView):
    form_class = RegistrationRequestForm
    template_name = "website/registration/request.html"

class RegistrationRequestSuccessView(View):
    def get(self, request):
        return render(request, "website/registration/request_success.html")
