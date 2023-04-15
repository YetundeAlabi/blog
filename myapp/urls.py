from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("myapp/<int:pk>", views.SinglePageView.as_view(), name="post-detail")
]