from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from Users.models import User, Profile
from Blog.models import Post
from django import forms


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

    username = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-3'
            }
        )
    )

    first_name = forms.CharField(
        required=False,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Type your name here...'
            }
        )
    )

    last_name = forms.CharField(
        required=False,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Type your surname here...'
            }
        )
    )


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

    image = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                'class': 'form-control mb-3',
            }
        )
    )


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

    title = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3',
        })
    )

    slug = forms.SlugField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3',
        })
    )

    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control mb-3',
        })
    )