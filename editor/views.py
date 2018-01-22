from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, FormView
#from django.views.generic.base import RedirectView, TemplateView
from . import models


class ArticlesView: pass


class ArticleView: pass


class CreateArticle(CreateView):
    template_name = 'editor\create.html'
    model = models.Articles
    fields = ['name', 'text', 'likes', 'dislikes']
    success_url = '/'
    
    def get_context_data(self, **kwargs):
        context = super(CreateArticle, self).get_context_data(**kwargs)
        context['postTo'] = self.kwargs['pk']
        return context
    
    def form_valid(self, form):
        form.instance.blog = models.Blogs.objects.get(pk=self.kwargs['pk'])
        return super(CreateArticle, self).form_valid(form)


class UpdateArtice(UpdateView): pass


class DeleteArticle: pass
