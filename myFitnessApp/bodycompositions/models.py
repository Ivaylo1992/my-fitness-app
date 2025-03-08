from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from myFitnessApp.utils.mixins import HasUserMixin, TimeStampedMixin


class BodyCompositionLog(TimeStampedMixin, HasUserMixin):
    weight = models.FloatField(
        validators=(
            MinValueValidator(0),
            MaxValueValidator(499.9)
        )
    )

    body_fat = models.FloatField(
        validators=(
            MinValueValidator(0),
            MaxValueValidator(99.9)
        ),
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'Body composition log made on {self.created_at.date()}'


class BodyMeasurements(TimeStampedMixin, HasUserMixin):
    neck = models.FloatField(
        validators=(
            MinValueValidator(0),
            MaxValueValidator(49.9)
        ),
        null=True,
        blank=True,
    )

    chest = models.FloatField(
        validators=(
            MinValueValidator(0),
            MaxValueValidator(149.9)
        ),
        null=True,
        blank=True,
    )

    biceps = models.FloatField(
        validators=(
            MinValueValidator(0),
            MaxValueValidator(99.9)
        ),
        null=True,
        blank=True,
    )

    waist = models.FloatField(
        validators=(
            MinValueValidator(0),
            MaxValueValidator(299.9)
        ),
        null=True,
        blank=True,
    )

    hips = models.FloatField(
        validators=(
            MinValueValidator(0),
            MaxValueValidator(299.9)
        ),
        null=True,
        blank=True,
    )

    thigh =models.FloatField(
        validators=(
            MinValueValidator(0),
            MaxValueValidator(99.9)
        ),
        null=True,
        blank=True,
    )

    calf =models.FloatField(
        validators=(
            MinValueValidator(0),
            MaxValueValidator(99.9)
        ),
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'Body Measurement Log created on {self.created_at.date()}'