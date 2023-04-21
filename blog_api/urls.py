from rest_framework import generics
from myapp.models import Post, Contact, Comment, Category
from .serializers import PostSerializer, CategorySerializer, ContactSerializer, CommentSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDestroy(generics.DestroyAPIView):
    queryset = Post.object.all()
    serializer_class = PostSerializer
    

class CreateCategory(generics.CreateAPIView):
    serializer_class = CategorySerializer
