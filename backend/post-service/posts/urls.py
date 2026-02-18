from django.urls import path
from .views import PostCreateView, PostListView, MyPostListView, PostDetailView, PostDeleteView, PostUpdateView, CommentListView, CommentCreateView, CommentDeleteView, CommentDetailView, CommentUpdateView, MyCommentListView

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('list/', PostListView.as_view(), name='post-list'),
    path('my-posts/', MyPostListView.as_view(), name='my-posts'),
    path('detail/<int:post_id>/', PostDetailView.as_view(), name='post-detail'),
    path('update/<int:post_id>/', PostUpdateView.as_view(), name='post-update'),
    path('delete/<int:post_id>/', PostDeleteView.as_view(), name='post-delete'),


    path('<int:post_id>/comments/create/', CommentCreateView.as_view(), name='comment-create'),
    path('<int:post_id>/comments/', CommentListView.as_view(), name='comment-list'),
    path('comments/my-comments/', MyCommentListView.as_view(), name='my-comment'),
    path('comments/detail/<int:comment_id>/', CommentDetailView.as_view(), name='comment-detail'),
    path('comments/update/<int:comment_id>/', CommentUpdateView.as_view(), name='comment-update'),
    path('comments/delete/<int:comment_id>/', CommentDeleteView.as_view(), name='comment-delete'),
]

