from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class TimeStampedMixin:
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )


class HasUserMixin:
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )