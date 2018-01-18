from django.conf.urls import url
from . import views

app_name = 'access'
urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(), name='logAUserIn'),
    url(r'^registration/$', views.RegistrationView.as_view(), name='registration'),
    url(r'^logout/$', views.logAUserOut, name='logout')
]
