from django.conf.urls import url, include
from django.views.generic import TemplateView, ListView

from website import views
from website.views import EventListView

urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name="home-site/home.html"), name="home"),

    url(r'^events/$', EventListView.as_view(), name="event-list"),

    # url(r'^(?P<url>.*/)$', include('django.contrib.flatpages.urls')),
]