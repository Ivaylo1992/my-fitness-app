from rest_framework import serializers

from myFitnessApp.workouts.models import Exercise, ExerciseLog, WorkoutLog


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


class ExerciseLogSerializer(serializers.ModelSerializer):
    exercise_name = serializers.CharField(source='exercise.name', read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = ExerciseLog
        fields = (
            'id',
            'exercise',
            'exercise_name',
            'sets',
            'repetitions',
            'rest_time',
            'notes',
            'user',
            'created_at',
            'updated_at',
        )

        read_only_fields = ("created_at", "updated_at")

        extra_kwargs = {
            'exercise': {'write_only': True},
        }


class WorkoutLogSerializer(serializers.ModelSerializer):
    exercise_logs = ExerciseLogSerializer(many=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = WorkoutLog
        
        fields = (
            'id',
            'name',
            'exercise_logs',
            'created_at',
            'updated_at',
            'user',
        )

        read_only_fields = ("created_at", "updated_at")

        read_only_fields = ('created_at', 'updated_at')

    
    def create(self, validated_data):
        logs_list = []
        exercise_logs_data = validated_data.pop('exercise_logs', [])
        workout_log = WorkoutLog.objects.create(**validated_data)

        for exercise_log_data in exercise_logs_data:
            logs_list.append(ExerciseLog(**exercise_log_data, user=workout_log.user))
        
        if logs_list:
            logs_list = ExerciseLog.objects.bulk_create(logs_list)
            print(logs_list)
            workout_log.exercise_logs.set(logs_list)
            
        return workout_log


    
