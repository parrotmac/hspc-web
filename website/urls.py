from django.conf.urls import url
from website.views import EventListView, RegistrationRequestView, RegistrationRequestSuccessView, AnnouncementListView, \
    NewsListView

app_name = 'website'

urlpatterns = [
    url(r'^events/$', EventListView.as_view(), name="event-list"),
    url(r'^announcements/$', AnnouncementListView.as_view(), name='announcement-list'),
    url(r'^newsroom/$', NewsListView.as_view(), name='newsroom-list'),

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
]
