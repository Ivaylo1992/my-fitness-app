from django.contrib import admin

from myFitnessApp.workouts.models import Exercise, ExerciseLog, WorkoutLog

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', 'muscle_group', 'equipment')

    list_filter = ('equipment', 'muscle_group')

    search_fields = ('name', 'muscle_group')


@admin.register(ExerciseLog)
class ExerciseLogAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', 'user')

    list_filter = ('created_at', )

    search_fields = ('user__email', )


@admin.register(WorkoutLog)
class WorkoutLogAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', 'user')

    list_filter = ('created_at', )

    search_fields = ('user__email', )