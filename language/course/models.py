from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    full_name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.full_name} {self.email}'

