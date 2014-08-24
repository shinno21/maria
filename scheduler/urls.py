# -*- coding: utf-8 -*-
# __author__ = 'shinno21'
from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'maria.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.schedule_list , name='scheduler_toppage'),

)
