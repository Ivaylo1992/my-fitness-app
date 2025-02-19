from rest_framework import serializers

from myFitnessApp.food.models import Food

class FoodSerializer(serializers.ModelSerializer):
    protein = serializers.DecimalField(max_digits=5, decimal_places=2)
    
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