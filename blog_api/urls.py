from django.urls import path, include
from blog_api import views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'), # obtain authentication token for user
    path('users', views.UserCreate.as_view(), name='user_create'), # register user
    path('login', views.LoginView.as_view(), name='login'), # login user
    path('posts', views.PostList.as_view(), name='post_list'), # list all posts
    path('posts/<int:pk>', views.PostDetail.as_view(), name='post_detail'), # retrieve single post by id
    path('posts/<int:pk>/comments', views.CommentList.as_view(), name='comment_list'),
    path('comments/<int:pk>', views.CommentDetail.as_view(), name='comment_detail'),
    path('categories', views.CategoryList.as_view(), name='categories'),
    path('categories/<int:pk>/posts', views.CategoryDetail.as_view(), name='category_detail'), # retrieve category by name
    path('contact', views.ContactView.as_view(), name='contact'), # send contact message
]
