

from django.test import TestCase
from unittest.mock import patch
from django.utils.timezone import datetime
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
    

    def test__save_method__assigns_workout_name(self):
        '''Assigning of the correct workout name is tested in the save_workout_name test'''

        workout_names = [
            "Morning Workout",
            "Noon Workout",      
            "Afternoon Workout", 
            "Night Workout",     
            "Midnight Workout",  
            "Midnight Workout"
        ]

        self.assertIn(self.workout_log.name, workout_names)

    def test__str_method(self):
        expected_value = 'Morning Workout made on 2025-03-14'

        self.assertEqual(str(self.workout_log), expected_value)