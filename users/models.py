from django.contrib.auth.models import AbstractUser
from django.db import models

from config import NULLABLE


# Create your models here.

class User(AbstractUser):
    """Implementation of the user model."""

    username = None
    email = models.EmailField(
        unique=True,
        verbose_name='email'
    )

    first_name = models.CharField(
        max_length=150,
        **NULLABLE,
        verbose_name="first name"
    )
    last_name = models.CharField(
        max_length=150,
        **NULLABLE,
        verbose_name="last name"
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return f'{self.email}'
