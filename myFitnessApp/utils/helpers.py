def save_workout_name(obj):
    time_related_names = {
        (1, 11): 'Morning',
        (11, 12): 'Noon',
        (13, 17): 'Afternoon',
        (17, 23): 'Night',
        (23, 23): 'Midnight',
    }

    for time_range, workout_name in time_related_names.items():
        if obj.updated_at in range(*time_range):
            obj.name = f'{workout_name} Workout'