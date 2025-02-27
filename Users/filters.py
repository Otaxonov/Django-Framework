from Blog.models import Post
from django import forms
import django_filters


class PostFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = ['title']

    title = django_filters.CharFilter(
        label='By Title',
        lookup_expr='icontains',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Search Posts by Title'
            }
        )
    )