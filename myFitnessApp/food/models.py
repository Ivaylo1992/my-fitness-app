from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator

UserModel = get_user_model()

class Food(models.Model):
    FOOD_NAME_MAX_LENGTH = 80
    SERVING_SIZE_UNIT_MAX_LENGTH = 2

    food_name = models.CharField(
        max_length=FOOD_NAME_MAX_LENGTH
    )

    protein = models.FloatField(
        validators=(MinValueValidator(0) ,)
    )

    carbohydrates = models.FloatField(
        validators=(MinValueValidator(0) ,)
    )

    fats = models.FloatField(
        validators=(MinValueValidator(0) ,)
    )

    calories = models.FloatField()

    serving_size_unit = models.CharField(
        max_length=SERVING_SIZE_UNIT_MAX_LENGTH
    )

    serving_size = models.PositiveSmallIntegerField()

    def save(self, *args, **kwargs):
        self.calories = (self.protein * 4) + (self.carbohydrates * 4) + (self.fats * 9)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.food_name


# class FoodLog(models.Model):
#     food = models.ForeignKey(
#         to=Food,
#         on_delete=models.DO_NOTHING,
#         related_name='logs',
#     )

#     user = models.ForeignKey(
#         to=UserModel,
#         on_delete=models.CASCADE,
#         related_name='logs'
#         )

#     quantity = models.FloatField(
        
#     )