import urllib.parse

from django.contrib.auth import get_user_model
from django.shortcuts import redirect


def get_or_auto_create_user(user_info):
    User = get_user_model()
    user, created = User.objects.get_or_create(username=user_info['sub'])
    user.first_name = user_info['given_name']
    user.last_name  = user_info['family_name']
    user.email      = user_info['email']
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    user.save()
    return user

def oidc_login_redirect(request):

    next_url_from_qs = request.GET.get("next")
    if next_url_from_qs:
        next_query_string = next_url_from_qs
    else:
        next_query_string = request.path

    problematic_redirect_urls = ['/auth', '/cms/login', '/auth/logout', '/admin/login', '/admin/logout']

    if next_query_string.rstrip("/") in problematic_redirect_urls:
        next_query_string = None

    if next_query_string:
        return redirect("/auth/?next=" +  urllib.parse.quote_plus(next_query_string))
    return redirect("/auth/")

def oidc_logout_redirect(request):
    return redirect("/auth/logout/")
