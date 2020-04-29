from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from . forms import PostForm, CommentForm, ProjectForm
from . models import Post, User, Comment, Project
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            descriptione = request.POST.get('description')
            title = request.POST.get('title')
            project_form = Project.objects.create(title=title, author=request.user, description=descriptione)
            project_form.save()
            return redirect('home')
    else:
        form = ProjectForm()
    
    variable ='variable'

    return render(request, 'app/project_create.html', {'form':form , 'variable' : variable})
    

class ProjectCreate(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'app/project_create.html'
    fields = ['title','description',]

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
    fields = ['title','description',]
    
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
    comments = Comment.objects.filter(post=post).order_by('-id')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            content = request.POST.get('content')
            comment = Comment.objects.create(post=post, author = request.user, content=content)
            comment.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else :
        form = CommentForm()

    stuff_for_frontend = {
        'object' : post,
        'comments': comments,
        'form' :form,
    }

    return render(request, 'app/post_detail.html', stuff_for_frontend)
    
class ProjectDetail(DetailView):
    model = Project 
    template_name = 'app/project_detail.html'

def ProjectDetail1(request, pk):
    project = get_object_or_404(Project, pk=pk)
    projectid = Project.objects.filter(pk=pk).first().id
    
    stuff_for_frontend = {
        'project' : project,
        'projectid': projectid,
    }
    return render(request, 'app/project_detail.html',stuff_for_frontend)
