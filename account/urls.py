from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path(r'', views.account, name='account')
]
