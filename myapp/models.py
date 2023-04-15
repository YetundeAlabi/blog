from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, help_text="Enter post category")

    def __str__(self):
        return self.name

class Comment(models.Model):
    text = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.text
    

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
    categories = models.ManyToManyField(Category)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="post_comments", blank=True, null=True)
    num_of_read = models.PositiveIntegerField(default=0)
    # image = models.ImageField()

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title
    


