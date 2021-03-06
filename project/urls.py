"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'main.views.home', name='home'),

    url(r'^blog/$', 'main.views.blog_list', name='blog_list'),
    url(r'^blog/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<entry_slug>[-\w]+)/$', 'main.views.blog_details', name='blog_details'),

    url(r'^projects/$', 'main.views.project_list', name='project_list'),
    url(r'^projects/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<entry_slug>[-\w]+)/$', 'main.views.project_details', name='project_details'),

    url(r'^about/$', 'main.views.about', name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
