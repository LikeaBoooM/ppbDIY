from django.urls import path

from . import views
from .views import PostList, PostCreate, PostDelete, PostUpdate, PostDetail, ProjectCreate, ProjectView

urlpatterns = [
    path('', views.home , name='home'),
    #path('project/create', ProjectCreate.as_view(), name='project-create'),
    path('project/create', views.add_project, name='project-create'),
    path('posts/', PostList.as_view(), name='posts'),
    path('projects/', ProjectView.as_view(), name='projects'),
    path('post/create/', PostCreate.as_view(), name='post-create'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post-delete'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post-update'),
    path('post/<int:pk>/', views.PostDetail, name ='post_detail')
]