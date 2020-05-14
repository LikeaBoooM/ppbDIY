from django import forms
from . models import Post, CommentProject,CommentPost, Project

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class CommentFormProject(forms.ModelForm):
    class Meta:
        model = CommentProject
        fields = ['content']

class CommentFormPost(forms.ModelForm):
    class Meta:
        model = CommentPost
        fields = ['content']


class ProjectForm(forms.ModelForm):
    #miniature = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':'trool'}))
    class Meta:
        model = Project
        fields = ['title','miniature','description',]