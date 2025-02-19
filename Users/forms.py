from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from Blog.models import Post
from Users.models import User
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SignInForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'content']
