from django import forms
from . models import Post, Comment, Project

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title','miniature','description',]