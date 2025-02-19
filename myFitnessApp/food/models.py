from django.db import models

class Food(models.Model):
    FOOD_NAME_MAX_LENGTH = 80
    SERVING_SIZE_UNIT_MAX_LENGTH = 2

    food_name = models.CharField(
        max_length=FOOD_NAME_MAX_LENGTH
    )

    protein = models.FloatField()

    carbohydrates = models.FloatField()

    fats = models.FloatField()

    calories = models.FloatField()

    serving_size_unit = models.CharField(
        max_length=SERVING_SIZE_UNIT_MAX_LENGTH
    )

    serving_size = models.SmallIntegerField()

    def save(self, *args, **kwargs):
        self.calories = (self.protein * 4) + (self.carbohydrates * 4) + (self.fats * 9)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.food_name
