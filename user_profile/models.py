import django.utils.timezone
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from datetime import datetime, timezone

class UserManager(BaseUserManager):
    """
    Customizing user creation
    """
    def create_user(self, username, email, password, **kwargs):
        """
        :param username:username
        :param email: email address
        :param password: login password
        :param kwargs:***
        :return:Create and return a `User` with an email, username and password.
        """
        if username is None:
            raise TypeError('Users must have a username.')
        if email is None:
            raise TypeError('Users must have an email.')
        if password is None:
            raise TypeError('Users must have an password.')
        first_name, last_name, middle_name = kwargs.get('first_name'), kwargs.get('last_name'), kwargs.get('middle_name')
        user = self.model(username=username, email=self.normalize_email(email), first_name=first_name,
                          last_name=last_name, middle_name=middle_name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')
        if email is None:
            raise TypeError('Superusers must have an email.')
        if username is None:
            raise TypeError('Superusers must have an username.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractUser, PermissionsMixin):
    """
    Customized Django User model
    """
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created  = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now = True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField( max_length=255, null=True, blank=True)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"
