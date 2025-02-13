from django.shortcuts import render
from django.views import View
from Blog.models import Post

# Create your views here.


class HomeView(View):
    template_name = 'blog/home.html'
    context = {'title': 'Blog App'}

    def get(self, request, *args, **kwargs):
        return render(request=request, template_name=self.template_name, context=self.context)


class PostsView(View):
    template_name = 'blog/posts.html'
    context = {'title': 'Posts'}

    def get(self, request, *args, **kwargs):
        self.context['posts'] = Post.objects.all()
        return render(request=request, template_name=self.template_name, context=self.context)
