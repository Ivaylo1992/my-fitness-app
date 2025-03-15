from django.utils.timezone import now, localtime

def save_workout_name() -> str:
    time_related_names = {
        (1, 11): 'Morning',
        (11, 13): 'Noon',
        (13, 17): 'Afternoon',
        (17, 23): 'Night',
        (23, 24): 'Midnight',
        (0, 1): 'Midnight',
    }

    for time_range, workout_name in time_related_names.items():
        update_hour = localtime(now()).hour

        if update_hour in range(*time_range):
            name = f'{workout_name} Workout'
            break
    
    return name
