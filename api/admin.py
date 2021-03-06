from django.contrib import admin
from .models import Urls


class UrlsAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'pub_date')
    ordering = ('-pub_date',)


# Register the Urls model with UrlsAdmin options
admin.site.register(Urls, UrlsAdmin)
