import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, View

from hspc_home.settings import LOGIN_URL
from website.forms import RegistrationRequestForm
from website.models import EventCategory, Announcement, NewsMention


class EventListView(ListView):

    model = EventCategory
    template_name = "website/events.html"

    def get_context_data(self, **kwargs):
        return super(EventListView, self).get_context_data(**kwargs)


class AnnouncementListView(ListView):
    model = Announcement
    template_name = "website/announcements.html"
    queryset = Announcement.objects.order_by('-created')

    def get_context_data(self, **kwargs):
        return super(AnnouncementListView, self).get_context_data(**kwargs)


class NewsListView(ListView):
    model = NewsMention
    template_name = 'website/newsroom.html'


class RegistrationRequestView(CreateView):
    form_class = RegistrationRequestForm
    template_name = "website/registration/request.html"

class RegistrationRequestSuccessView(View):
    def get(self, request):
        return render(request, "website/registration/request_success.html")



def account_profile_overview(request):
    return render(request, "website/accounts/profile.html", {"login_url": LOGIN_URL})
