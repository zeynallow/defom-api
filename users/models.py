from django.contrib.auth.models import AbstractUser
from django.db import models

class account(AbstractUser):
    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.email
