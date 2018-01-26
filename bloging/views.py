from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . import models


class BlogsView(ListView):
    template_name = 'bloging\listBlog.html'
    model = models.Blogs


class BlogView(DetailView):
    template_name = 'bloging\detailBlog.html'
    model = models.Blogs
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        if self.object.owner == self.request.user.profiles:
            context['isOwner'] = True
        else:
            context['isOwner'] = False
        return context


class CreateBlog(CreateView):
    template_name = 'bloging\createBlog.html'
    model = models.Blogs
    fields = ['name', 'picture', 'about', 'subscribers']

    def form_valid(self, form):
        form.instance.owner = self.request.user.profiles
        return super(CreateBlog, self).form_valid(form)


class UpdateBlog(UpdateView):
    template_name = 'bloging\\updateBlog.html'
    model = models.Blogs
    fields = ['name', 'picture', 'about']


class DeleteBlog(DeleteView):
    template_name = 'bloging\deleteBlog.html'
    model = models.Blogs
    success_url = '/'
