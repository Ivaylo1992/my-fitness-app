from django.test import TestCase
from freezegun import freeze_time
from myFitnessApp.utils.factories import ExerciseLogFactory, UserModelFactory


class ExerciseLogTest(TestCase):
    def setUp(self):
        self.user = UserModelFactory()
        self.exercise_log = ExerciseLogFactory(user=self.user)

    
    def test__model_labels(self):
        """Testing all fields labels of the model with subTest"""

        field_labels = {
            'exercise': 'exercise',
            'repetitions': 'repetitions',
            'weight': 'weight',
            'rest_time': 'rest time',
            'notes': 'notes',
            'user': 'user',
            'created_at': 'created at',
            'updated_at': 'updated at'
        }
    
        for field, expected_label in field_labels.items():
            with self.subTest(field=field):
                current_label = self.exercise_log._meta.get_field(field).verbose_name
                self.assertEqual(current_label, expected_label)
        
    def test__str_method(self):
        expected_output = 'Exercise log made on 2025-03-14'

        with freeze_time('2025-03-14 18:45:00'):
            exercise_log = ExerciseLogFactory(user=self.user)
            self.assertEqual(str(exercise_log), expected_output)