from django.db import models
from django.contrib.auth.models import AbstractUser


USER_TYPE_CHOICES = (("admin", "admin"), ("staff", "staff"), ("manager", "manager"))


class CustomUser(AbstractUser):
    app_user_type = models.CharField(max_length=20, blank=True, null=True, choices=USER_TYPE_CHOICES)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=13, null=True, blank=True)

    def __str__(self):
        return self.username
