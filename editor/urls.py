from django.urls import path, include
from . import views


app_name = 'article'

extra_urlpatterns = [
    path(r'', views.ArticleView.as_view(), name='article'),
    path(r'update/', views.UpdateArticle.as_view(), name='update'),
    path(r'delete/', views.DeleteArticle.as_view(), name='delete')
]

urlpatterns = [
    path(r'/create/', views.CreateArticle.as_view(), name='create'),
    path(r's/', views.ArticlesView.as_view(), name='articles'),
    path(r'/<int:article_id>/', include(extra_urlpatterns))
]
