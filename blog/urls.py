from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blogengin.views.index'),
    url('post_add', 'blogengin.views.post_form'),
    url(r'^post/detail/(?P<slug>[\w\-]+)/$', 'blogengin.views.post', name='blog_detail'),
    url(r'^post/detail/(?P<slug>[\w\-]+)/edit/$', 'blogengin.views.post_form'),
    url(r'^post/list/(?P<cid>[\w\-]+)/$', 'blogengin.views.list'),

    url('register', 'blogengin.views.register_user'),
)
