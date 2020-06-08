from django.http import HttpResponseRedirect
from django.contrib.auth import login
from django.views.generic.edit import CreateView


from . import forms
from account import models


class RegistrationView(CreateView):
    template_name = 'userAccess/registration.html'
    form_class = forms.User_Creation_Form
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        models.Profile(username=user).save()
        login(self.request, user)
        return HttpResponseRedirect(self.success_url)
