from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$',views.post_list,name='post_list' ),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/pricefilter/d/$',views.price_filter_d,name='price_filter_d'),
    url(r'^post/pricefilter/a/$', views.price_filter_a, name='price_filter_a'),

    url(r'^post/tvfilter/$', views.tv_filter, name='tv_filter'),
    url(r'^post/acfilter/$', views.ac_filter, name='ac_filter'),

]
