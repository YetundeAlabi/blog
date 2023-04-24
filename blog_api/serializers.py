from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from myapp.models import Post, Category, Comment, Contact

class CategorySerializer(serializers.ModelSerializer):
    post = serializers.ReadOnlyField(read_only=True)
    class Meta:
        model = Category
        fields =["name", "post"]



class PostSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Post
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    post = PostSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ['name', "text", "post"]




class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ["name", "email", "subject", "message"]


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data["email"],
            username=validated_data["username"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
