from django.conf.urls import url
from . import views


app_name = 'article'

urlpatterns = [
    url(r'^/create/$', views.CreateArticle.as_view(), name='create'),
    #url(r'^/(?P<id>[0-9]+)/update/$', views.UpdateArticle.as_view(), name='update'),
    #url(r'^/(?P<id>[0-9]+)/delete/$', views.DeleteArticle.as_view(), name='delete'),
    #url(r'^s/$', views.ArticlesView.as_view(), name='articles'),
    #url(r'^/(?P<id>[0-9]+)/$', views.ArticleView.as_view(), name='article')
]
