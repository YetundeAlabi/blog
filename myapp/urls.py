from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("/<int:pk>", views.SinglePageView.as_view(), name="post-detail"),
    path('/contact/', views.ContactView.as_view(), name='contact'),
]