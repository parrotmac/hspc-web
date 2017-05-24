from django.conf.urls import url, include
from django.views.generic import TemplateView

from website import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="home-site/home.html"), name="home"),

    url(r'^(?P<url>.*/)$', include('django.contrib.flatpages.urls')),
]