from django.urls import path
from Blog.views import (
    HomeView
)

urlpatterns = [
    path('', HomeView.as_view(), name='blog_home')
]
