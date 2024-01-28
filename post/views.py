from rest_framework import generics, permissions
from .models import Post, Comment, Share, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer, ShareSerializer

from django.shortcuts import get_object_or_404


class PostListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        own_posts = Post.objects.filter(user=user)
        shared_posts = Post.objects.filter(shared_post__user=user)

        # Combine own posts and shared posts
        queryset = own_posts.union(shared_posts)

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [permissions.IsAuthenticated]
    
    
    
class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        post_id = self.request.data.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(user=self.request.user, post=post)

class LikeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ShareListCreateAPIView(generics.ListCreateAPIView):
    queryset = Share.objects.all()
    serializer_class = ShareSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)