from django.urls import path
from .views import PostCreateView, PostListView, MyPostListView, PostDetailView, PostDeleteView, PostUpdateView

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('list/', PostListView.as_view(), name='post-list'),
    path('my-posts/', MyPostListView.as_view(), name='my-posts'),
    path('detail/<int:post_id>/', PostDetailView.as_view(), name='post-detail'),
    path('update/<int:post_id>/', PostUpdateView.as_view(), name='post-update'),
    path('delete/<int:post_id>/', PostDeleteView.as_view(), name='post-delete'),
]