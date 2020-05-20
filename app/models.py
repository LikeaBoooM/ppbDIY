from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from ckeditor_uploader.fields import RichTextUploadingField
#from . models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=40, unique=True)
    

    def __str__(self):
        return str(self.content)
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super(Post, self).save(*args, **kwargs)
        

class Project(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    miniature = models.ImageField(upload_to='static/', default='static/arduino.jpg')
    description = RichTextUploadingField(blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)


    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Project, self).save(*args, **kwargs)
    
    def upload_image(self, filename):
        return 'post/{}/{}'.format(self.title, filename)

    def total_likes(self):
        return self.likes.count()


class CommentPost(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ddate_posted = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.author.username


class CommentProject(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ddate_posted = models.DateTimeField(default=timezone.now)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.author.username
       