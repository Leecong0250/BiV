# -*- coding:utf-8 -*-
from django.conf.urls import patterns, url
from login.views import Login

urlpatterns = patterns(
    '',
     url(r'^$',Login.as_view(), name='login'),
)
