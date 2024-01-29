from django.urls import path
from .views import (
    PostListCreateAPIView, PostDetailAPIView, CommentListCreateAPIView, LikeListCreateAPIView, ShareListCreateAPIView
)

urlpatterns = [
    # Posts
    path('list/', PostListCreateAPIView.as_view(), name='post-list-create'),
    path('list/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),

    # Comments
    path('comments/', CommentListCreateAPIView.as_view(), name='comment-list-create'),

    # Likes
    path('likes/', LikeListCreateAPIView.as_view(), name='like-list-create'),

    # Shares
    path('shares/', ShareListCreateAPIView.as_view(), name='share-list-create'),

    # Add more URL patterns as needed
]
