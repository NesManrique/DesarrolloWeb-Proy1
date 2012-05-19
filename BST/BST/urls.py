from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from user_manager.views import *
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_bookmarks.views.home', name='home'),
    # url(r'^django_bookmarks/', include('django_bookmarks.foo.urls')),
    (r'^$', main_page),
    (r'^users/$', users),
    (r'^users/(\w+)/$', user_page),
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', user_logout),
    (r'^registro/$', register_page),
    (r'^registro/exitoso/$', direct_to_template, {'template': 'registration/registro_exitoso.html'}),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
