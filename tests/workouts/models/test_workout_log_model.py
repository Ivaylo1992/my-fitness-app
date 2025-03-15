from django.test import TestCase
from freezegun import freeze_time
from myFitnessApp.utils.factories import ExerciseLogFactory, UserModelFactory, WorkoutLogFactory
from myFitnessApp.workouts.models import WorkoutLog


class WorkoutLogTest(TestCase):
    def setUp(self):
        self.user = UserModelFactory()
        self.exercise_log = ExerciseLogFactory(user=self.user)
        self.workout_log = WorkoutLogFactory(user=self.user)
        self.workout_log.exercise_logs.set([self.exercise_log])
        
    def test__model_labels(self):
        """Testing all fields labels of the model with subTest"""

        field_labels = {
            'name': 'name',
            'exercise_logs': 'exercise logs',
            'user': 'user',
            'created_at': 'created at',
            'updated_at': 'updated at'
        }
    
        for field, expected_label in field_labels.items():
            with self.subTest(field=field):
                current_label = self.workout_log._meta.get_field(field).verbose_name
                self.assertEqual(current_label, expected_label)
    

    def test__save_method__assigns_correct_workout_name(self):
        hour_cases = [
            (6, "Morning Workout"),    # 6 AM → Morning
            (12, "Noon Workout"),      # 12 PM → Noon
            (15, "Afternoon Workout"), # 3 PM → Afternoon
            (19, "Night Workout"),     # 7 PM → Night
            (23, "Midnight Workout"),  # 11 PM → Midnight
            (0, "Midnight Workout"),   # 12 AM → Midnight
        ]

        for hour, workout_name in hour_cases:
            with freeze_time(f'2025-03-14 {hour}:00:00'):
                workout = WorkoutLog.objects.create(user=self.user)
                self.assertEqual(workout.name, workout_name)

    def test__str_method(self):
        expected_value = 'Morning Workout made on 2025-03-14'

        with freeze_time(f'2025-03-14 06:00:00'):
            workout = WorkoutLog.objects.create(user=self.user)
            self.assertEqual(str(workout), expected_value)