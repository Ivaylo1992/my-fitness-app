from django.db import models


class Exercise(models.Model):
    class MuscleGroupChoices(models.TextChoices):
        ABDOMINALS = 'Abdominals'
        ABDUCTORS = 'Abductors'
        BICEPS = 'Biceps'
        CALVES = 'Calves'
        CHEST = 'Chest'
        FOREARMS = 'Forearms'
        GLUTES = 'Glutes'
        HAMSTRINGS = 'Hamstrings'
        LATS = 'Lats'
        LOWER_BACK = 'Lower back'
        MIDDLE_BACK = 'Middle back'
        NECK = 'Neck'
        QUADRICEPS = 'Quadriceps'
        TRAPS = 'Traps'
        TRICEPS = 'Triceps'
        OTHER = 'Other'

    NAME_MAX_LENGTH = 50
    MUSCLE_GROUP_MAX_LENGTH = max([len(x) for _, x in MuscleGroupChoices.choices])

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    muscle_group = models.CharField(
        max_length=MUSCLE_GROUP_MAX_LENGTH,
        choices=MuscleGroupChoices.choices,
        default=MuscleGroupChoices.OTHER
    )

    exercise_picture = models.URLField(
        null=True,
        blank=True,
    )

    exercise_video = models.URLField(
        null=True,
        blank=True
    )

    instructions = models.TextField(
        null=True,
        blank=True
    )