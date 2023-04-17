from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("categories/<int:category_id>/posts/<int:pk>", views.SinglePageView.as_view(), name="post-detail"),
    path('contact/', views.contact, name='contact'),
    path('<int:pk>/comment', views.add_comment_to_post, name="comment")
]