from django.db import models
from home.models import CustomUser


class Contact(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=255, blank=False, null=False)
    mobile = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(blank=True, null=True)
    spam = models.BooleanField(default=False)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
