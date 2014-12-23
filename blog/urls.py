from django.conf.urls import patterns, include, url
from . import views


urlpatterns = patterns('',
    url(r'^$', views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name="post_detail"),
    url(r'^post/new/$', views.post_new, name="post_new"),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name="post_edit"),
    url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name="post_remove"),
    url(r'^post/(?P<post_id>[0-9]+)/comment/new/$', views.comment_new, name="comment_new"),
)
