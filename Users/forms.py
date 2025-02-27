from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from Blog.models import Post
from Users.models import User
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3'
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control mb-3'
        })
    )
    password1 = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control mb-3'
        })
    )
    password2 = forms.CharField(
        label='Password Confirmation',
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control mb-3'
        })
    )


class SignInForm(AuthenticationForm):
    username = forms.CharField(
        label='Username',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3'
        })
    )
    password = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control mb-3'
        })
    )


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'content']

    title = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': 'Enter Post Title Here...'
        })
    )

    slug = forms.SlugField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': 'Enter Post Slug Here...'
        })
    )

    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control mb-3',
            'placeholder': 'Enter Post Content Here...'
        })
    )


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'content']
