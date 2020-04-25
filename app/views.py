from django.shortcuts import render
from django.http import HttpResponse
from . forms import PostForm
from . models import Post, User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.

def home(request):
    if request.method == "POST" :
        form = PostForm(request.POST or None)
        if form.is_valid():
            form.save()

    return render(request, 'app/home.html')

class PostList(ListView):
    model = Post
    template_name = 'app/home.html'
    context_object_name = 'posts'

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image']
    template = 'app/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDetail(DetailView):
    model = Post  
    