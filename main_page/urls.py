from django.urls import path
from . import views

app_name = 'main_page'

urlpatterns = [
    path(r'', views.main_page, name='main')
]
