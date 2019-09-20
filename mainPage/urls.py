from django.urls import path, include
from . import views

app_name = 'mainPage'

urlpatterns = [
    path(r'', views.mainPage, name='main'),
    # path(r'', include('userAccess.urls'))
]
