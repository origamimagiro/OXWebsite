from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get/(\w+)/$', views.bro_info, name='info')
]