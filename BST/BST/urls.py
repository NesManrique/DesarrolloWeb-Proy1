from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from user_manager.views import *
from error_manager.views import *
from error_manager.models import *
from django.views.generic import DetailView, ListView
from django.views.generic.simple import direct_to_template
from django.utils.encoding import force_unicode
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from user_manager import admin_snippet
from user_manager import in_group_snippet

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_bookmarks.views.home', name='home'),
    # url(r'^django_bookmarks/', include('django_bookmarks.foo.urls')),
    url(r'^$', main_page, name="main_page"),
    url(r'^users/$', users),
    url(r'^users/(\w+)/$', user_page),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', user_logout),
    url(r'^registro/$', register_page),
    url(r'^registro/exitoso/$', direct_to_template, {'template': 'registration/registro_exitoso.html'}),
    url(r'^error/save/$', error_save),
    url(r'^error/save/exitoso/$', direct_to_template, {'template': 'error_save_exitoso.html'}),
    url(r'^error/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Error,
            template_name='error_detail.html')),
    url(r'^error/list/(\w+)/$', ErrorsListView.as_view()) ,
    url(r'^error/listu/(\w+)/$', error_list) ,
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^tag/([^\s]+)/$', tag_page),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
     'document_root': settings.MEDIA_ROOT}))
