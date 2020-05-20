from django.urls import path

from . import views
from .views import PostList, PostCreate, CommentProjectDelete, PostDelete, CommentPostDelete, PostUpdate, PostDetail, ProjectCreate, ProjectView, ProjectUpdate, ProjectDetail, ProjectDelete

urlpatterns = [
    path('', views.home , name='home'),
    #path('project/create', ProjectCreate.as_view(), name='project-create'),
    path('project/create', views.add_project, name='project-create'),
    path('posts/', PostList.as_view(), name='posts'),
    path('projects/', ProjectView.as_view(), name='projects'),
    path('post/create/', PostCreate.as_view(), name='post-create'),
    path('post/<int:pk>/delete/', PostDelete.as_view(), name='post-delete'),
    path('post/<int:pk>/update/', PostUpdate.as_view(), name='post-update'),
    path('post/<slug:slug>/', views.PostDetail, name='post-detail'),
    path('post/<int:pk>/delete/comment', CommentPostDelete.as_view(), name='comment-post-delete'),
    path('project/<int:pk>/update/', ProjectUpdate.as_view(), name='project-update'),
    path('project/<int:pk>/', views.ProjectDetail, name='project-detail'),
    path('project/<int:pk>/delete/comment', CommentProjectDelete.as_view(), name='comment-project-delete'),
    path('project/<int:pk>/delete/', ProjectDelete.as_view(), name='project-delete'),
    
]