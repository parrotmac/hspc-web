import urllib.parse

from django.contrib.auth import get_user_model
from django.shortcuts import redirect


def get_or_auto_create_user(user_info):
    User = get_user_model()
    user, created = User.objects.get_or_create(username=user_info.get('sub'))
    user.is_active = True
    user.first_name = user_info.get('given_name', "")
    user.last_name = user_info.get('family_name', "")
    user.email = user_info.get('email', "")
    user.is_staff = True
    user.is_superuser = True
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    user.save()
    return user


def oidc_login_redirect(request):
    # Imported locally to prevent startup issues
    from hspc_home.settings import LOGIN_URL

    next_url_from_qs = request.GET.get("next")
    if next_url_from_qs:
        next_query_string = next_url_from_qs
    else:
        next_query_string = request.path

    problematic_redirect_urls = ['/cms/login', '/auth/logout', '/admin/login', '/admin/logout']
    problematic_redirect_urls += LOGIN_URL

    if next_query_string.rstrip("/") not in problematic_redirect_urls:
        return redirect(LOGIN_URL + "?next=" + urllib.parse.quote_plus(next_query_string))

    return redirect(LOGIN_URL)


def oidc_logout_redirect(request):
    return redirect("/auth/logout/")
