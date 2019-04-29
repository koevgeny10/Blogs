from django.urls import path, re_path
from . import views


app_name = 'article'

urlpatterns = [
    path(r'/create/', views.CreateArticle.as_view(), name='create'),
    re_path(r'^/(?P<id>[0-9]+)/update/$', views.UpdateArticle.as_view(), name='update'),
    re_path(r'^/(?P<id>[0-9]+)/delete/$', views.DeleteArticle.as_view(), name='delete'),
    path(r's/', views.ArticlesView.as_view(), name='articles'),
    re_path(r'^/(?P<id>[0-9]+)/$', views.ArticleView.as_view(), name='article')
]
