from rest_framework import serializers

from myFitnessApp.food.models import Food, FoodLog


class FoodLogSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = FoodLog
        fields = ("food", "quantity", "user", "created_at", "updated_at")
        read_only_fields = ("created_at", "updated_at")
        

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = (
            "food_name",
            "protein",
            "carbohydrates",
            "fats",
            "serving_size",
            "serving_size_unit",
            "calories",
        )

        read_only_fields = ("calories",)
