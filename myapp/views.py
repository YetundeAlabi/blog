from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import FormView

from .forms import ContactForm, CommentForm, SearchForm
from .models import Post, Category, Comment

# Create your views here.


class CategoryFilterMixin:
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(category_id=self.kwargs.get('category_id'))


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
        context["slider_post"] = Post.objects.order_by('?')[:4]
        Post.objects.filter(author=self.request.user)
        Post.objects.filter(author_id=self.request.user.id)

        return context


class PostListView(ListView):
    model = Post
    template_name = "index.html"


class SinglePageView(CategoryFilterMixin, DetailView):
    model = Post
    template_name= "myapp/single-page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        related_posts = Post.objects.filter(categories__in=self.object.categories.all()).exclude(pk=self.object.pk)
        context['related_posts'] = related_posts
        context['categories'] = Category.objects.all()
        return context
    
    def get_object(self, queryset=None):
        post = super().get_object(queryset=queryset)
        post.num_of_read += 1
        post.save()
        return post


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for contacting us. Your message has been sent.')
            return redirect('index')
    else:
        form = ContactForm()
    return render(request, 'myapp/contact.html', {'form': form})


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            # comment.author = request.user
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'myapp/post_comment.html', {'form': form})


def search(request):
    query = request.GET.get('q')

    if query:
        results = Post.objects.filter(title__icontains=query)
    else:
        results = None

    form = SearchForm()

    context = {
        'results': results,
        'form': form,
        'query': query
    }

    return render(request, 'search.html', context)

