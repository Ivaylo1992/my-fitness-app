from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator

from myFitnessApp.utils.helpers import save_workout_name
from myFitnessApp.utils.mixins import HasUserMixin, TimeStampedMixin

UserModel = get_user_model()

class Exercise(models.Model):
    class EquipmentChoices(models.TextChoices):
        DUMBBELL = 'dumbbell'
        BODYWEIGHT = 'bodyweight'
        BARBELL = 'barbell'
        CABLE = 'cable'
        E_Z_CURL_BAR = 'e-z curl bar'
        MACHINE = 'machine'
        BANDS = 'bands'
        OTHER = 'other' 


    class MuscleGroupChoices(models.TextChoices):
        ABDOMINALS = 'abdominals'
        ABDUCTORS = 'abductors'
        BICEPS = 'biceps'
        CALVES = 'calves'
        CHEST = 'chest'
        FOREARMS = 'forearms'
        GLUTES = 'glutes'
        HAMSTRINGS = 'hamstrings'
        LATS = 'lats'
        LOWER_BACK = 'lower back'
        MIDDLE_BACK = 'middle back'
        NECK = 'neck'
        QUADRICEPS = 'quadriceps'
        TRAPS = 'traps'
        TRICEPS = 'triceps'
        OTHER = 'other'
    
    class Meta:
        ordering = ['name']

    NAME_MAX_LENGTH = 50
    MUSCLE_GROUP_MAX_LENGTH = max([len(x) for _, x in MuscleGroupChoices.choices])
    EQUIPMENT_MAX_LENGTH = max([len(x) for _, x in EquipmentChoices.choices])

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(MinLengthValidator(5),)
    )
    

    muscle_group = models.CharField(
        max_length=MUSCLE_GROUP_MAX_LENGTH,
        choices=MuscleGroupChoices.choices,
        default=MuscleGroupChoices.OTHER
    )

    equipment = models.CharField(
        max_length=EQUIPMENT_MAX_LENGTH,
        choices=EquipmentChoices.choices,
        default=EquipmentChoices.OTHER,
    )

    exercise_picture = models.URLField(
        null=True,
        blank=True,
    )

    exercise_video = models.URLField(
        null=True,
        blank=True
    )

    # TODO: fix video and picture field

    instructions = models.TextField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class ExerciseLog(HasUserMixin, TimeStampedMixin, models.Model):
    NOTES_MAX_LENGTH = 50

    exercise = models.ForeignKey(
        to=Exercise,
        on_delete=models.CASCADE,
    )

    repetitions = models.PositiveSmallIntegerField()

    weight = models.PositiveSmallIntegerField()

    rest_time = models.PositiveSmallIntegerField(
        null=True,
        blank=True
    )

    notes = models.TextField(
        max_length=NOTES_MAX_LENGTH,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'Exercise log made on {self.created_at.date()}'

class WorkoutLog(TimeStampedMixin, HasUserMixin):

    class Meta:
        ordering = ['-created_at']

    exercise_logs = models.ManyToManyField(
        to=ExerciseLog,
        related_name='workouts',
    )

    name = models.CharField(
        null=False,
        blank=True,
    )

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = save_workout_name()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} made on {self.created_at.date()}'






