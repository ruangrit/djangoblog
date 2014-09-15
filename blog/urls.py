from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blogengin.views.index'),
     url('post_form', 'blogengin.views.post_form'),
    url(r'^(?P<slug>[\w\-]+)/$', 'blogengin.views.post'),
)
