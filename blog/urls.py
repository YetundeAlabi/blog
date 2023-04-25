"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("myapp/", include("myapp.urls")),
    path("api/", include("blog_api.urls"))
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('api/user_create', UserCreate.as_view()),
    # path('api-auth/', include('rest_framework.urls')),
    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'), # obtain authentication token for user
    # path('users/', UserCreate.as_view(), name='user_create'), # register user
    # path('api/login_user', LoginView.as_view(), name='login'), # login user
    # path('api/posts/', PostViewset.as_view({'get': 'list'}), name='post_list'), # list all posts
    # path('api/posts/<int:pk>/', PostViewset.as_view({'get': 'retrieve'}), name='post_detail'), # retrieve single post by id
    # path('api/posts/create/', PostListCreate.as_view(), name='post_create'), # create new post
    # path('api/posts/<int:pk>/update/', PostUpdateDestroyView.as_view(), name='post_update_delete'), # update or delete post by id
    # path('api/categories/<str:name>/posts', CategoryDetail.as_view(), name='category_detail'), # retrieve category by name
    # path('contact/', ContactView.as_view(), name='contact'), # send contact message
    # path('api/posts/<int:pk>/comments', CommentList.as_view(), name="comments")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
