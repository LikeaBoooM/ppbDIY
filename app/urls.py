from django.urls import path

from . import views
from .views import PostList, PostCreate, PostDelete, PostUpdate, PostDetail

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('create/', PostCreate.as_view(), name='post-create'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post-delete'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post-update'),
    path('<int:pk>/detail/', PostDetail.as_view(), name='post-detail'),
]