from django.conf.urls import url, include
from . import views


app_name = 'blog'

urlpatterns = [
    url(r'^/create/$', views.CreateBlog.as_view(), name='create'),
    url(r'^/(?P<pk>[0-9]+)/update/$', views.UpdateBlog.as_view(), name='update'),
    url(r'^/(?P<pk>[0-9]+)/delete/$', views.DeleteBlog.as_view(), name='delete'),
    url(r'^s/$', views.BlogsView.as_view(), name='blogs'),
    url(r'^/(?P<pk>[0-9]+)/$', views.BlogView.as_view(), name='blog'),
    url(r'^/(?P<pk>[0-9]+)/article', include('editor.urls'))
]
