from django.urls import path
from Users.views import (
    SignUpView, SignInView, SignOutView,
    PostsView, PostCreateView, PostEditView,
    PostDeleteView, AccountSettingsView
)

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='users_sign_up'),
    path('sign-in/', SignInView.as_view(), name='users_sign_in'),
    path('sign-out/', SignOutView.as_view(), name='users_sign_out'),
    path('settings/', AccountSettingsView.as_view(), name='account_settings'),
    path('posts/', PostsView.as_view(), name='users_posts'),
    path('post-create/', PostCreateView.as_view(), name='users_post_create'),
    path('post-edit/<slug:post_slug>/', PostEditView.as_view(), name='users_post_edit'),
    path('post-delete/<slug:post_slug>/', PostDeleteView.as_view(), name='users_post_delete'),
]
