from django.conf.urls import url, include
from . import views

app_name = 'mainPage'
urlpatterns = [
    url(r'^$', views.mainPage, name='main'),
    url(r'^', include('userAccess.urls'))
]
