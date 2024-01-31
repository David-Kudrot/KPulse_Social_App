from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PostListCreateAPIView, PostDetailAPIView, CommentListCreateAPIView, LikeListCreateAPIView, ShareListCreateAPIView, AllPostAPIViewsets, post_list_create_api_view
)


router = DefaultRouter()
router.register('list', AllPostAPIViewsets)



urlpatterns = [
    # Posts
    path('', include(router.urls)),
    path('lists/', PostListCreateAPIView.as_view(), name='post-list-create'),
    path('<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),
    path('makepost', post_list_create_api_view, name='makepost'),
    # Comments
    path('comments/', CommentListCreateAPIView.as_view(), name='comment-list-create'),

    # Likes
    path('likes/', LikeListCreateAPIView.as_view(), name='like-list-create'),

    # Shares
    path('shares/', ShareListCreateAPIView.as_view(), name='share-list-create'),

    # Add more URL patterns as needed
]
