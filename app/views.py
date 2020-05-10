from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from . forms import PostForm, CommentFormPost, CommentFormProject, ProjectForm
from . models import Post, User, CommentProject, CommentPost, Project
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user
            project.save() 
            return redirect('projects')
    else:
        form = ProjectForm()
    
    return render(request, 'app/project_create.html', {'form':form })

class ProjectCreate(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'app/project_create.html'
    fields = ['title','miniature','description',]

    def form_valid(self, form_class):
        post = form_class.save(commit=False)
        post.save()
        return HttpResponseRedirect(reverse('projects'))


class ProjectView(ListView):
    model = Project
    template_name = 'app/project_list.html'
    context_object_name = 'projects'

class PostList(ListView):
    model = Post
    template_name = 'app/posts.html'
    context_object_name = 'posts'

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template = 'app/post_form.html'
    

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    template_name = 'app/post_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
class ProjectDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    success_url = '/'
    template_name = 'app/project_delete.html'

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.author:
            return True
        return False

class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content',]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
        
class ProjectUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    fields = ['title','miniature','description',]
    template_name = 'app/project_update.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        project = self.get_object()
        if self.request.user == project.author:
            return True
        return False

def PostDetail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = CommentPost.objects.filter(post=post).order_by('-id')
    if request.method == 'POST':
        form = CommentFormPost(request.POST)
        if form.is_valid():
            content = request.POST.get('content')
            comment = CommentPost.objects.create(post=post, author = request.user, content=content)
            comment.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else :
        form = CommentFormPost()

    stuff_for_frontend = {
        'object' : post,
        'comments': comments,
        'form' :form,
    }

    return render(request, 'app/post_detail.html', stuff_for_frontend)

def ProjectDetail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    comments = CommentProject.objects.filter(project=project).order_by('-id')

    if request.method == 'POST':
        form = CommentFormProject(request.POST)
        if form.is_valid():
            content = request.POST.get('content')
            comment = CommentProject.objects.create(project=project, author=request.user, content=content)
            comment.save()
            return HttpResponseRedirect(project.get_absolute_url())
    else :
        form = CommentFormProject()
    
    stuff_for_frontend = {
        'object' : project,
        'comments' : comments,
        'form' : form,
    }

    return render(request, 'app/project_detail.html', stuff_for_frontend)
    

