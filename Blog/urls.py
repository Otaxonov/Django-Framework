from django.urls import path
from Blog.views import (
    HomeView, PostsView
)

urlpatterns = [
    path('', HomeView.as_view(), name='blog_home'),
    path('posts/', PostsView.as_view(), name='blog_posts'),
]
