from rest_framework import serializers

from myFitnessApp.food.models import Food, FoodLog


class FoodLogSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = FoodLog
        fields = ("food", "quantity", "user")


class FoodSerializer(serializers.ModelSerializer):
    logs = FoodLogSerializer(many=True, read_only=True)

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
            "logs",
        )

        read_only_fields = ("calories",)
