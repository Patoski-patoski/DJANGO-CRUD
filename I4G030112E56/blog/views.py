# from django.shortcuts import render
from dataclasses import field
from django.views.generic import ListView

from blog.models import Post

# Create your views here.


class PostListView:
    
  queryset = Post.published.all()
  context_object_name = 'posts' # by default class list view uses object_list.
  paginate_by = 2   # number of objects/posts per page 
  template_name = 'pages/blog.html' # by default uses <appname>/<modelname>_<view_type>.html
model = Post

class PostListView(ListView):
    model = Post
    template_name = 'pages/blog.html'
    context_object_name = 'posts'
    paginate_by = 2
    ordering = ['-publish']
    def get_queryset(self):
        return Post.objects.filter(status='published')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog'
        return context

class PostCreateView(CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog:all')
    template_name = 'pages/post_form.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New Post'
        return context
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.object.slug})



class PostDetailView(DetailView):
    model = Post
    template_name = 'pages/post_detail.html'
    fields = '__all__'
    success_url = reverse_lazy('blog:all')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog'
        return context

class PostUpdateView(UpdateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog:all')
    template_name = 'pages/post_form.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Post'
        return context
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.object.slug})

class PostDeleteView(Update):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy('blog:all')
