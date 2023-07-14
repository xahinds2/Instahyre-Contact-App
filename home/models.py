from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    mobile = models.CharField(max_length=20, blank=False, null=False, unique=True)

    def __str__(self):
        return self.mobile
