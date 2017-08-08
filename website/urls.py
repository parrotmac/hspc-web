from django.conf.urls import url
from django.urls import reverse

from website.api import EventsApi
from website.views import EventListView, RegistrationRequestView, RegistrationRequestSuccessView

urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name="home-site/home.html"), name="home"),

    url(r'^events/$', EventListView.as_view(), name="event-list"),

    url(
        r'^membership/join/request/submitted/$',
        RegistrationRequestSuccessView.as_view(),
        name="registration-request-submitted"
    ),

    url(
        r'^membership/join/request/$',
        RegistrationRequestView.as_view(success_url="/membership/join/request/submitted/"),  # Can't use reverse() since the urlspatterns aren't built yet
        name="registration-request"
    ),

    # Just so we have a starting point in the future
    url(r'^api/v1/event/?$', EventsApi.as_view()),
    url(r'^api/v1/event/(?P<event_id>[0-9]+)/?$', EventsApi.as_view()),

    # url(r'^(?P<url>.*/)$', include('django.contrib.flatpages.urls')),
]