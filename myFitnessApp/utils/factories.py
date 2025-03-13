import factory
from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory

from myFitnessApp.food.models import Food
from myFitnessApp.workouts.models import Exercise

UserModel = get_user_model()

class UserFactory(factory.Factory):
    class Meta:
        model = UserModel

    email = 'ivo@app.com'


class AdminFactory(factory.Factory):
    class Meta:
        model = UserModel

    email = 'ivo2@app.com'
    is_staff = True
    is_superuser = True


class FoodFactory(DjangoModelFactory):
    class Meta:
        model = Food

    food_name = 'test_name'
    protein = 20
    carbohydrates = 10
    fats = 10
    serving_size_unit = 'g'
    serving_size = 100


class ExerciseFactory(DjangoModelFactory):
    class Meta:
        model = Exercise

    name = 'Test exercise'
    muscle_group = 'biceps'
    equipment = 'barbell'
    instructions = 'test instructions'