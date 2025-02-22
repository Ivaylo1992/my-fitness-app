from rest_framework import serializers

from myFitnessApp.food.models import Food, FoodLog




class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = (
            'food_name',
            'protein',
            'carbohydrates',
            'fats',
            'serving_size',
            'serving_size_unit',
            'calories'
            )
        
        read_only_fields = ('calories', )


class FoodLogSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    food = serializers.PrimaryKeyRelatedField(queryset=Food.objects.all())

    class Meta:
        model = FoodLog
        fields = ('food', 'quantity', 'user')