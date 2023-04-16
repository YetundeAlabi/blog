from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .models import Post, Category, Comment
# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        context["post_list"] = Post.objects.all()[:4]
        context["categories"] = Category.objects.all()[:4]
        context["latest_post"] = Post.objects.order_by('-date_created')[:3]
        context["popular_post"] = Post.objects.order_by('-num_of_read')[:3]
        context["featured_post"] = Post.objects.order_by('?')[:3]

        return context


class PostListView(ListView):
    model = Post
    template_name = "index.html"


class SinglePageView(DetailView):
    model = Post
    template_name= "myapp/single-page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # related_category = self.object.categories.first()
        # related_posts = Post.objects.filter(categories=related_category).exclude(pk=self.object.pk)
        # context['related_category'] = related_category
        # context['related_posts'] = related_posts
        related_posts = Post.objects.filter(categories__in=self.object.categories.all()).exclude(pk=self.object.pk)
        context['related_posts'] = related_posts
        return context
    
    def get_object(self, queryset=None):
        post = super().get_object(queryset=queryset)
        post.num_of_read += 1
        post.save()
        return post



