# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin

try:
    from django.conf.urls import patterns

    urlpatterns = patterns('',
        url(r'^admin_mountpoint/', include(admin.site.urls)),
    )
except ImportError:
    # Django 1.10+
    from django.core.exceptions import ImproperlyConfigured

    try:
        urlpatterns = [
            url(r'^admin_mountpoint/', include(admin.site.urls)),
        ]
    except ImproperlyConfigured:
        # Django 2.0+
        from django.urls import path

        urlpatterns = [
            path('admin/', admin.site.urls),
        ]
