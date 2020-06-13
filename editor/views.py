from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from . import models
from blogs.models import Blog
from utils.my_module import get_login_url


def test_for_articles(self):
    self.blog = Blog.objects.get(id=self.kwargs.get('blog_id'))
    return self.request.user == self.blog.owner.user


class ArticlesView(ListView):
    template_name = 'editor/articles.html'
    model = models.Article
    
    def get_queryset(self):
        blog_id = self.kwargs.get('blog_id')
        if blog_id:
            self.queryset = models.Article.objects.filter(
                blog=Blog.objects.get(id=blog_id)
            )
        return super().get_queryset()


class ArticleView(DetailView):
    template_name = 'editor/article.html'
    model = models.Article
    context_object_name = 'article'
    pk_url_kwarg = 'article_id'


class CreateArticle(UserPassesTestMixin, CreateView):
    template_name = 'editor/create.html'
    model = models.Article
    fields = ['name', 'text']
    test_func = test_for_articles
    get_login_url = get_login_url
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_id'] = self.kwargs.get('blog_id')
        return context
    
    def form_valid(self, form):
        form.instance.blog = self.blog  # TODO !
        return super().form_valid(form)


class UpdateArticle(UserPassesTestMixin, UpdateView):
    template_name = 'editor/update.html'
    model = models.Article
    fields = ['name', 'text']
    pk_url_kwarg = 'article_id'
    test_func = test_for_articles
    get_login_url = get_login_url


class DeleteArticle(UserPassesTestMixin, DeleteView):
    template_name = 'editor/delete.html'
    model = models.Article
    pk_url_kwarg = 'article_id'
    success_url = '/'
    test_func = test_for_articles
    get_login_url = get_login_url
