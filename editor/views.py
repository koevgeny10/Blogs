from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, FormView
#from django.views.generic.base import RedirectView, TemplateView
from . import models


class CreateArticle(CreateView):
    template_name = 'editor\create.html'
    model = models.Articles
    fields = ['name', 'text']
    success_url = '/'
    
#    def post(self, request, *args, **kwargs):
#        print(self.request.POST)
#        print('++++++++++++')
#        print(self.request.FILES)
#        return HttpResponseRedirect(self.success_url)


class UpdateArtice(UpdateView): pass
