from django.urls import path

from . import views
from .views import PostList, PostCreate, PostDelete, PostUpdate, PostDetail, ProjectCreate, ProjectView, ProjectUpdate, ProjectDetail, ProjectDelete

urlpatterns = [
    path('', views.home , name='home'),
    #path('project/create', ProjectCreate.as_view(), name='project-create'),
    path('project/create', views.add_project, name='project-create'),
    path('posts/', PostList.as_view(), name='posts'),
    path('projects/', ProjectView.as_view(), name='projects'),
    path('post/create/', PostCreate.as_view(), name='post-create'),
    path('post/<int:pk>/delete/', PostDelete.as_view(), name='post-delete'),
    path('post/<int:pk>/update/', PostUpdate.as_view(), name='post-update'),
    path('post/<int:pk>/', views.PostDetail, name ='post-detail'),
    path('project/<int:pk>/update/', ProjectUpdate.as_view(), name='project-update'),
    path('project/<int:pk>/', ProjectDetail.as_view(), name ='project-detail'),
    path('project/<int:pk>/delete/', ProjectDelete.as_view(), name ='project-delete'),
]