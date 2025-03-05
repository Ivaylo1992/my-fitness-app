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
    id = serializers.IntegerField(required=False)
    exercise_name = serializers.CharField(source='exercise.name', read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = ExerciseLog
        fields = (
            'id',
            'exercise',
            'exercise_name',
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

    
    def get_or_create_exercise_logs(self, exercise_logs, user):
        logs_pks = []

        for log in exercise_logs:
            log_instance, created = ExerciseLog.objects.get_or_create(
                pk=log.get('id'), user=user,defaults=log)
            logs_pks.append(log_instance.pk)

        return logs_pks
    
    def create_or_update_exercise_logs(self, exercise_logs, user):
        log_pks = []

        for log in exercise_logs:
            log_instance, created = ExerciseLog.objects.update_or_create(
                pk=log.get('id'), user=user, defaults=log
            )
            log_pks.append(log_instance.pk)

        return log_pks
    

    def create(self, validated_data):
        exercise_logs = validated_data.pop('exercise_logs', [])
        workout = WorkoutLog.objects.create(**validated_data)

        workout.exercise_logs.set(
            self.get_or_create_exercise_logs(exercise_logs=exercise_logs, user=workout.user))

        return workout

    def update(self, instance, validated_data):
        exercise_logs = validated_data.pop('exercise_logs', [])
        user = instance.user
        instance.exercise_logs.set(self.create_or_update_exercise_logs(
            exercise_logs=exercise_logs, user=user)
        )

        fields = ['id', 'name']

        for field in fields:
            try:
                setattr(instance, field, validated_data[field])
            except KeyError:
                pass

        instance.save()

        return instance

    

        



    
