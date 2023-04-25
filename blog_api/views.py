from django.conf import settings
from django.contrib.auth import authenticate
from django.core.mail import send_mail

from rest_framework import generics, permissions, status, filters
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from myapp.models import Post, Category, Comment, Contact
from blog_api.serializers import PostSerializer, CategorySerializer, CommentSerializer, ContactSerializer, UserSerializer, LoginSerializer
from blog_api.permissions import IsAuthorOrReadOnly


class UserCreate(generics.CreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = UserSerializer


class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    'token': token.key,
                    'user_id': user.pk,
                    'email': user.email
                })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostList(generics.ListCreateAPIView):
    """This mixin is used for creating a model instance of post by an authenticated user"""
    search_fields = ["content"]
    filter_backends = [filters.SearchFilter]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs["pk"]).all()


class CommentDetail(generics.RetrieveDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    permission_classes = [IsAuthorOrReadOnly]


class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class CategoryDetail(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(categories__id=self.kwargs["pk"])[:10]


class ContactView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            name = data.get("name")
            subject = data.get("subject")
            message = f"{data['message']} from {data['email']}"
            recipient_mail = ["yettybella7@gmail.com"]
            print(subject)
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=recipient_mail,
                fail_silently=False)
            return Response({"success": "Sent"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
