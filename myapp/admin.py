from django.contrib import admin
from myapp.models import Category, Comment, Post

# Register your models here.
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Post)

# class PostInline(admin.TabularInline):
#     model = Post
#     extra = 0


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     inlines = [PostInline]