from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views, forms

app_name = 'access'

urlpatterns = [
    path(r'registration/', views.RegistrationView.as_view(), name='registration'),

    path(r'login/', auth_views.LoginView.as_view(
        template_name='userAccess/login2.html',
        authentication_form=forms.LoginForm
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='userAccess/logout.html'
    ), name='logout'),

    path('password_change/', auth_views.PasswordChangeView.as_view(
        # template_name='userAccess/password_change_form.html'
    ), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', auth_views.PasswordResetView.as_view(
        # template_name='userAccess/password_reset_form.html',
        email_template_name='userAccess/password_reset_email.html',
        subject_template_name='userAccess/password_reset_subject.txt',
        success_url=reverse_lazy('mainPage:access:password_reset_done')
    ), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('mainPage:access:password_reset_complete')), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
