from django.contrib import admin

import website.models

admin.site.register(website.models.Event)
admin.site.register(website.models.MenuEntry)
