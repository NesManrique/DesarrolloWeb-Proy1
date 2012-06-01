from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.views.generic import DetailView
from error_manager.views import *

urlpatterns = patterns('error_manager.views',
    url(r'^save/$', error_save, name="save_error"),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Error,
            template_name='error_detail.html'),
            name="error_detail"),
    url(r'^(?P<error_id>\d+)/up_encargado/$', asignar_enc, name="up_encargado"),
    url(r'^(?P<error_id>\d+)/up_estado/$', asignar_estado, name="up_estado")
)
