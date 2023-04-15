from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Post, Category, Comment
# Create your views here.
class IndexView(TemplateView):
    template_name = 'my_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class SinglePageView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_category'] = Post.objects.filter(category = self.object.categories).exclude(pk=self.object.pk)
        return context



