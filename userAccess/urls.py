from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views, forms

urlpatterns = [
    path(
        r'registration/',
        views.RegistrationView.as_view(),
        name='registration'
    ),
    path(
        r'login/',
        auth_views.LoginView.as_view(authentication_form=forms.LoginForm),
        name='login'
    ),
    path('', include('django.contrib.auth.urls'))
]
