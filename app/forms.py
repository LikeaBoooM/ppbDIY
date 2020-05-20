from django import forms
from ckeditor_uploader.fields import RichTextUploadingField
from . models import Post, CommentProject,CommentPost, Project

class LoginForm(forms.ModelForm):
    Login = forms.CharField(label="Nazwa użytkownika")
    Password = forms.CharField(label="Hasło", widget=forms.PasswordInput)

    class Meta:
        fields = ['Login', 'Password', ]
class PostForm(forms.ModelForm):
    
    title = forms.CharField(label='Tytul')
    content = forms.CharField(label='Tresc', widget=forms.Textarea)

    class Meta:
        model = Post
        fields = ['title', 'content',]

class CommentFormProject(forms.ModelForm):
    content = forms.CharField(label='Nowy komentarz', widget=forms.Textarea)
    class Meta:
        model = CommentProject
        fields = ['content']

class CommentFormPost(forms.ModelForm):
    content = forms.CharField(label='Nowy komentarz', widget=forms.Textarea)
    class Meta:
        model = CommentPost
        fields = ['content']


class ProjectForm(forms.ModelForm):
    #miniature = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':'trool'}))
    title = forms.CharField(label='Tytul')
    miniature = forms.ImageField(label='Miniaturka projektu')
    class Meta:
        model = Project
        fields = ['title','miniature','Opis',]