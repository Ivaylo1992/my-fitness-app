from django.db import models


class Food(models.Model):
    MEAL_NAME_MAX_LENGTH = 80

    meal_name = models.CharField(
        max_length=MEAL_NAME_MAX_LENGTH
    )