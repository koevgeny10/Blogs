from django.conf.urls import url
from bloging.views import BlogView, BlogsView, DeleteBlog
from . import views


app_name = 'editor'
urlpatterns = [
    url(r'^$', BlogsView.as_view(), name='articles'),
    url(r'^(?P<pk>[0-9]+)/$', BlogView.as_view(), name='article'),
    url(r'create/$', views.CreateArticle.as_view(), name='create'),
    url(r'(?P<pk>[0-9]+)/update/$', views.UpdateArtice.as_view(), name='update'),
    url(r'(?P<pk>[0-9]+)/delete/$', DeleteBlog.as_view(), name='delete')
]
