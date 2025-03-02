from rest_framework import serializers

from myFitnessApp.workouts.models import Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = (
            'name',
            'muscle_group',
            'equipment',
            'exercise_picture',
            'exercise_video',
            'instructions',
        )