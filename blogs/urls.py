from django.urls import include, path
from . import views


app_name = 'blogs'

extra_urlpatterns = [
    path(r'', views.BlogView.as_view(), name='blog'),
    path(r'update/', views.UpdateBlog.as_view(), name='update'),
    path(r'delete/', views.DeleteBlog.as_view(), name='delete'),
    path(r'article', include('editor.urls'))
]

urlpatterns = [
    path(r'/create/', views.CreateBlog.as_view(), name='create'),
    path(r's/', views.BlogsView.as_view(), name='blogs'),
    path(r'/<int:blog_id>/', include(extra_urlpatterns))
]
