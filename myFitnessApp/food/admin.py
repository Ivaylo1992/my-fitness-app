from django.contrib import admin

from myFitnessApp.food.models import Food, FoodLog


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ("id", "food_name", "calories")


@admin.register(FoodLog)
class FoodLogAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', )

    list_filter = ('user', )

    search_fields = ('user__email', )
