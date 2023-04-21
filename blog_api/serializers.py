from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import serializers
from myapp.models import Post, Category, Comment, Contact

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        field =["name"]


class PostSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = Post
        field = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    post = PostSerializer(many=True, read_only=True)
    class Meta:
        model = Comment


class PostSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = Post
        field = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        field = "__all__"


class User(serializers.ModelSerializer):

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