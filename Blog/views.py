from django.shortcuts import render
from django.views import View

# Create your views here.


class HomeView(View):
    template_name = 'blog/home.html'
    context = {'title': 'Home View'}

    def get(self, request, *args, **kwargs):
        return render(request=request, template_name=self.template_name, context=self.context)
