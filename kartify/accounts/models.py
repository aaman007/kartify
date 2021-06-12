from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    pass


class User(AbstractUser):
    pass
