from datetime import datetime
from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, help_text="Enter post category")

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    subject = models.CharField(max_length=100, null=True)
    message = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    STATUS = (
    ("d", "Draft"),
    ("p", "Publish")
)
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')
    date_updated = models.DateTimeField(auto_now= True)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS, default="p", help_text="blog status")
    categories = models.ManyToManyField(Category, related_name="posts")
    num_of_read = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="myapp/images", null=True, height_field='img_height', width_field='img_width')
    img_height = models.PositiveIntegerField(null=True, blank=True, editable=True, default="223")
    img_width = models.PositiveIntegerField(null=True, blank=True, editable=True, default="350")

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post-detail", args=[str(self.id)])
    

class Comment(models.Model):
    name = models.CharField(max_length=50, default="anonymous", blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=True)
    text = models.CharField(max_length=200, blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

