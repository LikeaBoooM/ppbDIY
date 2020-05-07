from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
#from . models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.content
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)
        

class Project(models.Model):
    title = models.CharField(max_length=32, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    miniature = models.ImageField(default='static/arduino.jpg', upload_to='images')
    #description = RichTextField(blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Project, self).save(*args, **kwargs)

class CommentPost(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ddate_posted = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.author

class CommentProject(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ddate_posted = models.DateTimeField(default=timezone.now)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.author
       