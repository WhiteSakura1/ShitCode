from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=16,
        choises=(
            ('П' , "Пользователь"),
            ('А', "Администратор"),
            ('М', "Модератор"),
            ('Э', "Эксперт"),
        ),
        default="П"
    )
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
class Profile(models.Model):
    user = models.OneToOneField(
        User , on_delete=models.CASCADE
    )
    phone = models.CharField(
        max_length=32,
        unique=True

    )
    is_status = models.BooleanField(
        default=False,
        choices=(
            (False,'Базовый аккаунт'),
            (False,'Премиум аккаунт'),


        )
    )
