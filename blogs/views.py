from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . import models
from utils.my_module import get_login_url


test_for_blogs = lambda self: \
    self.request.user == self.get_object().owner.user


class BlogsView(ListView):
    template_name = 'blogs/listBlog.html'
    model = models.Blog


class BlogView(DetailView):
    template_name = 'blogs/detailBlog.html'
    model = models.Blog
    context_object_name = 'blog'
    pk_url_kwarg = 'blog_id'


class CreateBlog(LoginRequiredMixin, CreateView):
    template_name = 'blogs/createBlog.html'
    model = models.Blog
    fields = ['name', 'picture', 'about']

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile  # TODO !
        return super().form_valid(form)


class UpdateBlog(UserPassesTestMixin, UpdateView):
    template_name = 'blogs/updateBlog.html'
    model = models.Blog
    fields = ['name', 'picture', 'about']
    pk_url_kwarg = 'blog_id'
    test_func = test_for_blogs
    get_login_url = get_login_url


class DeleteBlog(UserPassesTestMixin, DeleteView):
    template_name = 'blogs/deleteBlog.html'
    model = models.Blog
    success_url = '/'
    pk_url_kwarg = 'blog_id'
    test_func = test_for_blogs
    get_login_url = get_login_url
