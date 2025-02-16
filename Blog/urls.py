from django.urls import path
from Blog.views import (
    HomeView, PostsView, PostView
)

urlpatterns = [
    path('', HomeView.as_view(), name='blog_home'),
    path('posts/', PostsView.as_view(), name='blog_posts'),
    path('posts/<slug:post_slug>/', PostView.as_view(), name='blog_post'),
]
