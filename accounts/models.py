from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        WAITER = "w", "Waiter"
        BILLING = "b", "Billing"
        KITCHEN = "k", "Kitchen"
        OWNER = "o", "Owner"

    role = models.CharField(
        max_length=2,
        choices=Role.choices,
        default=Role.WAITER,
    )