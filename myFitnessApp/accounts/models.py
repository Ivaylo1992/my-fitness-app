from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth import get_user_model

from myFitnessApp.accounts.managers import FitnessAppUserManager

class FitnessAppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = FitnessAppUserManager()

    def __str__(self):
        return self.email
    

UserModel = get_user_model()


class FitnessAppProfile(models.Model):
    FIRST_NAME_MAX_LENGTH = 50
    LAST_NAME_MAX_LENGTH = 50

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=FIRST_NAME_MAX_LENGTH
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=LAST_NAME_MAX_LENGTH
    )

    height = models.SmallIntegerField(
        null=True,
        blank=True,
    )

    weight = models.SmallIntegerField(
        null=True,
        blank=True,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )







