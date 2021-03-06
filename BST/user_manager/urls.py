from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from user_manager.views import *

urlpatterns = patterns('user_manager.views',
    url(r'^$', users, name="user_page"),
    url(r'^logout/$', user_logout, name="logout"),
    url(r'^login/$', user_login, name="login"),
    url(r'^registro/$', register_page),
    url(r'^lookup/$', user_lookup, name="get_users"),
    url(r'^(\w+)/$', user_page),
)
