from django.conf.urls import patterns, include, url
from telemetry_api import api, views

urlpatterns = patterns('',
        url(r'^$', views.index),
        url(r'^add-values/$', api.addValues, name='add_values'),
        url(r'^get-latest-values/$', api.getLatestValues, name='get_latest_values'),
        url(r'^get-values-by-id/$', api.getValuesById, name='get_values_by_id'),
        )