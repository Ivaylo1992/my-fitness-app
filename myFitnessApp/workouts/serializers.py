from rest_framework import serializers

from myFitnessApp.workouts.models import Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    short_instructions = serializers.SerializerMethodField()

    class Meta:
        model = Exercise
        fields = (
            'name',
            'muscle_group',
            'equipment',
            'exercise_picture',
            'exercise_video',
            'short_instructions',
        )

    def get_short_instructions(self, obj):
        return ' '.join(obj.instructions.split()[: 5]) + '...'