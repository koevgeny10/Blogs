from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . import models
from Blogs.myModule import getLoginUrl


testForBlogs = lambda self: self.request.user == self.get_object().owner.username


class BlogsView(ListView):
    template_name = 'bloging/listBlog.html'
    model = models.Blogs


class BlogView(DetailView):
    template_name = 'bloging/detailBlog.html'
    model = models.Blogs
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        if self.object.owner.username == self.request.user:
            context['isOwner'] = True
        else:
            context['isOwner'] = False
        return context


class CreateBlog(LoginRequiredMixin, CreateView):
    template_name = 'bloging/createBlog.html'
    model = models.Blogs
    fields = ['name', 'picture', 'about', 'subscribers']

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super(CreateBlog, self).form_valid(form)


class UpdateBlog(UserPassesTestMixin, UpdateView):
    template_name = 'bloging/updateBlog.html'
    model = models.Blogs
    fields = ['name', 'picture', 'about']
    
    test_func = testForBlogs
    
    get_login_url = getLoginUrl


class DeleteBlog(UserPassesTestMixin, DeleteView):
    template_name = 'bloging/deleteBlog.html'
    model = models.Blogs
    success_url = '/'
    
    test_func = testForBlogs
    
    get_login_url = getLoginUrl
