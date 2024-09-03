from django.contrib.auth.models import AbstractUser
from django.db import models

from config import NULLABLE


# Create your models here.

class User(AbstractUser):

    username = None
    email = models.EmailField(
        unique=True,
        verbose_name='email'
    )

    first_name = models.CharField(
        max_length=150,
        **NULLABLE,
        verbose_name="Имя"
    )
    last_name = models.CharField(
        max_length=150,
        **NULLABLE,
        verbose_name="Фамилия"
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return f'{self.email}'
