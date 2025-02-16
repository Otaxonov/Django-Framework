from Users.forms import SignUpForm, SignInForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views import View

# Create your views here.


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



