from django.contrib import admin

from myapp.models import Category, Comment, Post, Contact

# Register your models here.
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Contact)