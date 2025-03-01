from django.db import models


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

    NAME_MAX_LENGTH = 50
    MUSCLE_GROUP_MAX_LENGTH = max([len(x) for _, x in MuscleGroupChoices.choices])
    EQUIPMENT_MAX_LENGTH = max([len(x) for _, x in EquipmentChoices.choices])

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
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

    instructions = models.TextField(
        null=True,
        blank=True
    )