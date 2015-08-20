from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.all_brothers),
    url(r'^edit/$', views.update_profile),
    url(r'^profile/(\w+)/$', views.brother_profile)
]