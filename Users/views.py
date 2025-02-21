from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from Users.forms import SignUpForm, SignInForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from Users.forms import PostCreateForm, PostEditForm
from Blog.models import Post
from django.views import View

# Create your views here.


@method_decorator(login_required, name='dispatch')
class PostDeleteView(View):
    template_name = 'users/post/delete.html'
    context = {'title': 'Delete Post'}

    def get(self, request, *args, **kwargs):
        post = Post.objects.get(slug=kwargs['post_slug'], author=request.user)
        self.context['post'] = post
        return render(request=request, template_name=self.template_name, context=self.context)

    def post(self, request, *args, **kwargs):
        post = Post.objects.get(slug=kwargs['post_slug'], author=request.user)
        post.delete()
        return redirect('users_posts')


@method_decorator(login_required, name='dispatch')
class PostEditView(View):
    template_name = 'users/post/edit.html'
    context = {'title': 'Edit Post'}

    def get(self, request, *args, **kwargs):
        post = Post.objects.get(slug=kwargs['post_slug'])
        self.context['form'] = PostEditForm(instance=post)
        self.context['post'] = post
        return render(request=request, template_name=self.template_name, context=self.context)

    def post(self, request, *args, **kwargs):
        post = Post.objects.get(slug=kwargs['post_slug'])
        form = PostEditForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('users_post_edit', form.cleaned_data['slug'])
        self.context['form'] = form
        self.context['post'] = post
        return render(request=request, template_name=self.template_name, context=self.context)


@method_decorator(login_required, name='dispatch')
class PostCreateView(View):
    template_name = 'users/post/create.html'
    context = {'title': 'New Post'}

    def get(self, request, *args, **kwargs):
        self.context['form'] = PostCreateForm()
        return render(request=request, template_name=self.template_name, context=self.context)

    def post(self, request, *args, **kwargs):
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('users_posts')
        self.context['form'] = form
        return render(request=request, template_name=self.template_name, context=self.context)



@method_decorator(login_required, name='dispatch')
class PostsView(View):
    template_name = 'users/posts.html'
    context = {'title': 'My Posts'}

    def get(self, request, *args, **kwargs):
        posts = Post.objects.filter(author=request.user)
        self.context['posts'] = posts
        return render(request=request, template_name=self.template_name, context=self.context)

class SignInView(View):
    template_name = 'users/sign_in.html'
    context = {'title': 'Sign-In'}

    def get(self, request, *args, **kwargs):
        self.context['form'] = SignInForm()
        return render(request=request, template_name=self.template_name, context=self.context)

    def post(self, request, *args, **kwargs):
        form = SignInForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('blog_home')
        self.context['form'] = form
        return render(request=request, template_name=self.template_name, context=self.context)


class SignUpView(View):
    template_name = 'users/sign_up.html'
    context = {'title': 'Sign-Up'}

    def get(self, request, *args, **kwargs):
        self.context['form'] = SignUpForm()
        return render(request=request, template_name=self.template_name, context=self.context)

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_home')
        self.context['form'] = form
        return render(request=request, template_name=self.template_name, context=self.context)


class SignOutView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        return redirect('blog_home')
