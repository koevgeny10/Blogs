from django.urls import path
from . import views

app_name = 'profile'
urlpatterns = [
    path(r'', views.profile, name='profile')  # TODO '^' in path?
]
