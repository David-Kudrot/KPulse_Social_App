from rest_framework import generics, viewsets, permissions
from .models import Post, Comment, Share, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer, ShareSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class AllPostAPIViewsets(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



#post create korar jonno view
# views.py
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated]) # eta authentication er jonnno
def post_list_create_api_view(request):
    if request.method == 'GET':
        user = request.user
        own_posts = Post.objects.filter(user=user)
        shared_posts = Post.objects.filter(shared_post__user=user)
        queryset = own_posts.union(shared_posts)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class PostListCreateAPIView(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = self.request.user
        own_posts = Post.objects.filter(user=user)
        shared_posts = Post.objects.filter(shared_post__user=user)

        # Combine own posts and shared posts
        queryset = own_posts.union(shared_posts)

        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class PostListCreateAPIView(generics.ListCreateAPIView):
#     serializer_class = PostSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         user = self.request.user
#         own_posts = Post.objects.filter(user=user)
#         shared_posts = Post.objects.filter(shared_post__user=user)

#         # Combine own posts and shared posts
#         queryset = own_posts.union(shared_posts)

#         return queryset

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)



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
