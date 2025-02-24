from django.contrib import admin

from myFitnessApp.food.models import Food


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ("id", "food_name", "calories")
