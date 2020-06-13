from django.http import HttpResponseRedirect
from django.contrib.auth import login
from django.views.generic.edit import CreateView
from . import forms


class RegistrationView(CreateView):
    template_name = 'registration/registration.html'
    form_class = forms.MyUserCreationForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect(self.success_url)
