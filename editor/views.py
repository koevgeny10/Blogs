from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . import models
from bloging.models import Blogs


class ArticlesView(ListView):
    template_name = r'editor\articles.html'
    
    def get_queryset(self):
        self.queryset = models.Articles.objects.filter(blog__exact=Blogs.objects.get(pk=self.kwargs['pk']))
        return super(ArticlesView, self).get_queryset()


class ArticleView(DetailView):
    template_name = r'editor\article.html'
    model = models.Articles
    context_object_name = 'article'
    pk_url_kwarg = 'id'
    
    def get_context_data(self, **kwargs):
        context = super(ArticleView, self).get_context_data(**kwargs)
        if self.object.blog.owner == self.request.user.profiles:
            context['isOwner'] = True
        else:
            context['isOwner'] = False
        return context


class CreateArticle(CreateView):
    template_name = 'editor\create.html'
    model = models.Articles
    fields = ['name', 'text', 'likes', 'dislikes']
    
    def get_context_data(self, **kwargs):
        context = super(CreateArticle, self).get_context_data(**kwargs)
        context['postTo'] = self.kwargs['pk']
        return context
    
    def form_valid(self, form):
        form.instance.blog = models.Blogs.objects.get(pk=self.kwargs['pk'])
        return super(CreateArticle, self).form_valid(form)


class UpdateArticle(UpdateView):
    template_name = r'editor\update.html'
    model = models.Articles
    fields = ['name', 'text', 'likes', 'dislikes']
    pk_url_kwarg = 'id'


class DeleteArticle(DeleteView):
    template_name = 'editor\delete.html'
    model = models.Articles
    pk_url_kwarg = 'id'
    success_url = '/'
