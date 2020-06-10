from django.urls import include, path, re_path
from . import views


app_name = 'blog'

urlpatterns = [
    path(r'/create/', views.CreateBlog.as_view(), name='create'),
    re_path(r'^/(?P<pk>[0-9]+)/update/$', views.UpdateBlog.as_view(), name='update'),
    re_path(r'^/(?P<pk>[0-9]+)/delete/$', views.DeleteBlog.as_view(), name='delete'),
    path(r's/', views.BlogsView.as_view(), name='blogs'),
    re_path(r'^/(?P<pk>[0-9]+)/$', views.BlogView.as_view(), name='blog'),
    re_path(r'^/(?P<pk>[0-9]+)/article', include('editor.urls'))
]
