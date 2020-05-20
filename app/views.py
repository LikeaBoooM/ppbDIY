from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from . forms import PostForm, CommentFormPost, CommentFormProject, ProjectForm
from . models import Post, User, CommentProject, CommentPost, Project
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.urls import reverse
# Create your views here.


def home(request):
    projects = Project.objects.all().count()
    posts = Post.objects.all().count()

    posts_to_front = []
    projects_to_front = []
    likes_to_front = []

    if projects == 0:
        message = 'Cant find anything'
    elif projects == 1:
        project0 = Project.objects.order_by('-date_posted')[0]
        likes0 = project0.likes.count()
        likes_to_front.append(likes0)
        projects_to_front.append(project0)

    elif projects == 2:
        project0 = Project.objects.order_by('-date_posted')[0]
        project1 = Project.objects.order_by('-date_posted')[1]
        likes0 = project0.likes.count()
        likes1 = project1.likes.count()
        likes_to_front.append(likes0)
        likes_to_front.append(likes1)
        projects_to_front.append(project0)
        projects_to_front.append(project1)
    elif projects == 3:
        project0 = Project.objects.order_by('-date_posted')[0]
        project1 = Project.objects.order_by('-date_posted')[1]
        project2 = Project.objects.order_by('-date_posted')[2]
        likes0 = project0.likes.count()
        likes1 = project1.likes.count()
        likes2 = project2.likes.count()
        likes_to_front.append(likes0)
        likes_to_front.append(likes1)
        likes_to_front.append(likes2)
        projects_to_front.append(project0)
        projects_to_front.append(project1)
        projects_to_front.append(project2)
    elif projects > 3:
        project0 = Project.objects.order_by('-date_posted')[0]
        project1 = Project.objects.order_by('-date_posted')[1]
        project2 = Project.objects.order_by('-date_posted')[2]
        project3 = Project.objects.order_by('-date_posted')[3]
        projects_to_front.append(project0)
        projects_to_front.append(project1)
        projects_to_front.append(project2)
        projects_to_front.append(project3)
        likes0 = project0.likes.count()
        likes1 = project1.likes.count()
        likes2 = project2.likes.count()
        likes3 = project3.likes.count()
        likes_to_front.append(likes0)
        likes_to_front.append(likes1)
        likes_to_front.append(likes2)
        likes_to_front.append(likes3)

    if posts == 0:
        message = 'Cant find anything'
    elif posts == 1:
        post0 = Post.objects.order_by('-date_posted')[0]
        posts_to_front.append(post0)
    elif posts == 2:
        post0 = Post.objects.order_by('-date_posted')[0]
        post1 = Post.objects.order_by('-date_posted')[1]
        posts_to_front.append(post0)
        posts_to_front.append(post1)
    else:
        post0 = Post.objects.order_by('-date_posted')[0]
        post1 = Post.objects.order_by('-date_posted')[1]
        post2 = Post.objects.order_by('-date_posted')[2]
        posts_to_front.append(post0)
        posts_to_front.append(post1)
        posts_to_front.append(post2)

    stuff_for_frontend = {
        'posts_to_front': posts_to_front,
        'projects_to_front': projects_to_front,
        'likes_to_front' : likes_to_front,
    }
    return render(request, 'app/home.html', stuff_for_frontend)

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.EmailField(label='Nazwa użytkownika', widget=forms.TextInput)
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)
    
@login_required
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
    form_class = ProjectForm

    def form_valid(self, form_class):
        post = form_class.save(commit=False)
        post.save()
        return HttpResponseRedirect(reverse('projects'))


class ProjectView(ListView):
    model = Project
    template_name = 'app/project_list.html'
    context_object_name = 'projects'
    paginate_by = 6

class PostList(ListView):
    model = Post
    template_name = 'app/posts.html'
    context_object_name = 'posts'
    paginate_by = 10

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template = 'app/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentPostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CommentPost
    template_name = 'app/comment-post-delete.html'
    success_url = '/'
    
    def get_success_url(self):
        return reverse('post-detail', kwargs={'slug': self.object.post.slug})
        
    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author or self.request.user.is_superuser:
            return True
        return False


class CommentProjectDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CommentProject
    template_name = 'app/comment-project-delete.html'
    success_url = '/'

    def get_success_url(self):
        return reverse('project-detail', kwargs={'pk': self.object.project.id})

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author or self.request.user.is_superuser:
            return True
        return False


class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/posts'
    template_name = 'app/post_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author or self.request.user.is_superuser:
            return True
        return False

class ProjectDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    success_url = '/projects'
    template_name = 'app/project_delete.html'

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.author or self.request.user.is_superuser:
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
        if self.request.user == post.author or self.request.user.is_superuser:
            return True
        return False
        
class ProjectUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'app/project_update.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        project = self.get_object()
        if self.request.user == project.author or self.request.user.is_superuser :
            return True
        return False

def PostDetail(request, slug):
    post = get_object_or_404(Post, slug=slug)
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

    is_liked = False
    if project.likes.filter(pk=request.user.id).exists():
       is_liked = True

    stuff_for_frontend = {
        'object' : project,
        'comments' : comments,
        'form' : form,
        'is_liked' : is_liked,
        'total_likes' : project.total_likes(),
    }

    return render(request, 'app/project_detail.html', stuff_for_frontend)


def like_project(request):
    project = get_object_or_404(Project, id=request.POST.get('object_id'))
    is_liked = False
    if project.likes.filter(id=request.user.id).exists():
        project.likes.remove(request.user)
        is_liked = False
    else:
        project.likes.add(request.user)
        is_liked = True
    
    return HttpResponseRedirect(project.get_absolute_url())