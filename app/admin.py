from django.contrib import admin
from django.contrib.auth.models import User
from . models import Post, CommentPost, Project, CommentProject
# Register your models here

admin.site.register(Post)
admin.site.register(CommentProject),
admin.site.register(CommentPost),
admin.site.register(Project)