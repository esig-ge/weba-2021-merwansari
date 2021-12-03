from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, birth_date, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, birth_date, password=None):
        user = self.create_user(
            email,
            password=password,
            username=username,
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date
        )
        user.is_admin = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )

    username = models.CharField(max_length=32, unique=True)
    first_name = models.CharField(max_length=35, unique=False)
    last_name = models.CharField(max_length=35, unique=False)
    birth_date = models.DateField(auto_now_add=False)
    # games =
    is_active = models.BooleanField(default=True)
    is_coach = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'birth_date']

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

