from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .models import Post, Category, Comment
# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_list"] = Post.objects.all()
        context
        return context

class PostListView(ListView):
    model = Post
    template_name = "index.html"

class SinglePageView(DetailView):
    model = Post
    template_name= "myapp/single-page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_category'] = Post.objects.filter(category = self.object.categories).exclude(pk=self.object.pk)
        return context



