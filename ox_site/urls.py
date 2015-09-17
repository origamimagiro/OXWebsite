"""ox_site URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from people import urls as people_urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from . import views
from . import settings

urlpatterns = [
    url(r'^$', views.redirect),
    url(r'^main/', views.index),
    url(r'^brotherhood/', include(people_urls)),
    url(r'^rush/', views.rush),
    url(r'^events/', views.events),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^summer/', views.summer),
    url(r'^login/', views.login),
    url(r'^updatepassword/', views.update_password),
    url(r'^failed/', views.bad_login),
    url(r'^history/', views.history)
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
