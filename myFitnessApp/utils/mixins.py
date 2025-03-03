from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class TimeStampedMixin(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True


class HasUserMixin(models.Model):
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True
