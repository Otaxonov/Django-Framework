from django.urls import path
from Users.views import (
    SignUpView
)

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='users_sign_up')
]
