from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView, FormView
from . import forms
from account import models

import logging

logger = logging.getLogger(__name__)


class RegistrationView(CreateView):
    template_name = 'userAccess\\registration.html'
    model = User
    fields = ['username', 'email', 'password']
    success_url = '/'

    def form_valid(self, form):
        user = User.objects.create_user(username=form.instance.username,
                                        email=form.instance.email,
                                        password=form.instance.password)
        models.Profile(username=user).save()
        login(self.request, user)
        
        logger.debug('kek===========================================================================================================================================================================')
        
        return HttpResponseRedirect(self.success_url)


class LoginView(FormView):
    template_name = 'userAccess\login.html'
    form_class = forms.Login
    success_url = '/'

    def form_valid(self, form):
        if form.is_valid():
            user = authenticate(self.request, **form.cleaned_data)
            if user is not None:
                login(self.request, user)
                return HttpResponseRedirect(self.success_url)
            else:
                # Могут быть разные ошибки
                return self.form_invalid(form)
        return self.form_invalid(form)


def logAUserOut(request):
    '''Logout'''
    logout(request)
    return HttpResponseRedirect('/')
