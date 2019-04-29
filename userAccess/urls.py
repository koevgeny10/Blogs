from django.urls import path
from . import views

app_name = 'access'
urlpatterns = [
    path(r'login/', views.LoginView.as_view(), name='logAUserIn'),
    path(r'registration/', views.RegistrationView.as_view(), name='registration'),
    path(r'logout/', views.logAUserOut, name='logout')
]
