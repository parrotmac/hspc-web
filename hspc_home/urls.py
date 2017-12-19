"""hspc_home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import urllib.parse

from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.admin.views.decorators import staff_member_required

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls

import website.urls
from hspc_home import auth

# Required to trigger OIDC login page
admin.site.login = staff_member_required(admin.site.login)

urlpatterns = [

    url(r'^', include(website.urls.urlpatterns, namespace='website')),

    url(r'^auth/', include('django_auth_oidc.urls')),

    url(r'^admin/login', auth.oidc_login_redirect),
    url(r'^admin/logout', auth.oidc_logout_redirect),
    url(r'^admin/', admin.site.urls),

    url(r'^cms/login', auth.oidc_login_redirect),
    url(r'^cms/logout', auth.oidc_logout_redirect),
    url(r'^cms/', include(wagtailadmin_urls)),

    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'', include(wagtail_urls)),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
