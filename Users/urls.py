from django.urls import path
from Users.views import (
    SignUpView, SignInView, SignOutView,
    PostsView
)

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='users_sign_up'),
    path('sign-in/', SignInView.as_view(), name='users_sign_in'),
    path('sign-out/', SignOutView.as_view(), name='users_sign_out'),
    path('posts/', PostsView.as_view(), name='users_posts'),
]
