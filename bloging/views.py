from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . import models

# Чет странно
class BlogsView(ListView):
    template_name = 'bloging\listBlog.html'
    #model = models.Blogs
    
    def get_queryset(self):
        if self.request.path.startswith('/articles'):
            self.model = models.Articles
        else:
            self.model = models.Blogs
        return super(BlogsView, self).get_queryset()


class BlogView(DetailView):
    template_name = 'bloging\detailBlog.html'
    model = models.Blogs
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        print(self.object.owner == self.request.user.profiles)
        if self.object.owner == self.request.user.profiles:
            context['isOwner'] = True
        else:
            context['isOwner'] = False
        return context


class CreateBlog(CreateView):
    template_name = 'bloging\createBlog.html'
    model = models.Blogs
    fields = ['name', 'picture', 'about']
    #success_url = '/'
    
    def form_valid(self, form):
        form.instance.owner = self.request.user.profiles
        return super(CreateBlog, self).form_valid(form)


# Добавь проверку пользователя
class UpdateBlog(UpdateView):
    template_name = 'bloging\\updateBlog.html'
    model = models.Blogs
    fields = ['name', 'picture', 'about']
    success_url = '/'

#    def get_context_data(self, **kwargs):
#        context = super(UpdateBlog, self).get_context_data(**kwargs)
#        context['object'] = self.object
#        return context


class DeleteBlog(DeleteView):
    template_name = 'bloging\deleteBlog.html'
    model = models.Blogs
    success_url = '/'
