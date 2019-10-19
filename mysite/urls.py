# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from django.utils.translation import ugettext_lazy as _
from page_nav.admin import PageNavAdmin
from rest_framework.routers import DefaultRouter

admin.autodiscover()

urlpatterns = [
    url(r'^en/admin/page_nav/pagenav/likepost', PageNavAdmin.likePost),
    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url('', include('snippets.urls')),
    url('api-auth/', include('rest_framework.urls')),
]

urlpatterns += i18n_patterns(
    url(r'^admin/', admin.site.urls),  # NOQA
    #url(r'^', include('cms.urls'))
)

# Change admin site title
admin.site.site_header = _("ProjectAI Administration")
admin.site.site_title = _("ProjectAI Administration")

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ] + staticfiles_urlpatterns() + urlpatterns
