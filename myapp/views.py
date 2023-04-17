from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .models import Post, Category, Comment
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import ContactForm

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
        context["slider_post"] = Post.objects.order_by('?')[:2]

        return context


class PostListView(ListView):
    model = Post
    template_name = "index.html"


class SinglePageView(DetailView):
    model = Post
    template_name= "myapp/single-page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        related_posts = Post.objects.filter(categories__in=self.object.categories.all()).exclude(pk=self.object.pk)
        context['related_posts'] = related_posts
        return context
    
    def get_object(self, queryset=None):
        post = super().get_object(queryset=queryset)
        post.num_of_read += 1
        post.save()
        return post


class ContactView(FormView):
    template_name = 'myapp/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('success')

    
    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        # Send email or perform other processing
        return super().form_valid(form)



