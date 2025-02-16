from Users.forms import SignUpForm
from django.shortcuts import render, redirect
from django.views import View

# Create your views here.


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
