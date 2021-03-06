from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
import settings
import scheduler.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'maria.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', scheduler.views.schedule_list , name='scheduler_toppage'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^scheduler/', include('scheduler.urls')),
)

urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT,
    }),
)