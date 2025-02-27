from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(
        default='user/profile/default.png',
        upload_to='user/profile/images/'
    )

    def __str__(self):
        return f'{self.user.username} Profile'
