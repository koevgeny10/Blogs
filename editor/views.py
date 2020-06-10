from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from . import models
from bloging.models import Blogs
from Blogs.myModule import getLoginUrl


def testForArticles(self):
    self.blog = models.Blogs.objects.get(pk=self.kwargs['pk'])
    return self.request.user == self.blog.owner.username


class ArticlesView(ListView):
    template_name = 'editor/articles.html'
    
    def get_queryset(self):
        self.queryset = models.Articles.objects.filter(
                blog__exact=Blogs.objects.get(pk=self.kwargs['pk']))
        return super(ArticlesView, self).get_queryset()


class ArticleView(DetailView):
    template_name = 'editor/article.html'
    model = models.Articles
    context_object_name = 'article'
    pk_url_kwarg = 'id'
    
    def get_context_data(self, **kwargs):
        context = super(ArticleView, self).get_context_data(**kwargs)
        if self.object.blog.owner == self.request.user.profile:
            context['isOwner'] = True
        else:
            context['isOwner'] = False
        return context


class CreateArticle(UserPassesTestMixin, CreateView):
    template_name = 'editor/create.html'
    model = models.Articles
    fields = ['name', 'text', 'likes', 'dislikes']
    
    test_func = testForArticles
    
    get_login_url = getLoginUrl
    
    def get_context_data(self, **kwargs):
        context = super(CreateArticle, self).get_context_data(**kwargs)
        context['postTo'] = self.kwargs['pk']
        return context
    
    def form_valid(self, form):
        form.instance.blog = self.blog
        return super(CreateArticle, self).form_valid(form)


class UpdateArticle(UserPassesTestMixin, UpdateView):
    template_name = 'editor/update.html'
    model = models.Articles
    fields = ['name', 'text', 'likes', 'dislikes']
    pk_url_kwarg = 'id'
    
    test_func = testForArticles
    
    get_login_url = getLoginUrl


class DeleteArticle(UserPassesTestMixin, DeleteView):
    template_name = 'editor/delete.html'
    model = models.Articles
    pk_url_kwarg = 'id'
    success_url = '/'
    
    test_func = testForArticles
    
    get_login_url = getLoginUrl
