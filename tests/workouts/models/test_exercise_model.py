from django.test import TestCase

from myFitnessApp.utils.factories import ExerciseFactory


class ExerciseModelTest(TestCase):
    def setUp(self):
        self.exercise = ExerciseFactory()

    def test__model_labels(self):
        """Testing all fields labels of the model with subTest"""

        field_labels = {
            'name': 'name',
            'muscle_group': 'muscle group',
            'equipment': 'equipment',
            'exercise_picture': 'exercise picture',
            'exercise_video': 'exercise video',
            'instructions': 'instructions',
        }
    
        for field, expected_label in field_labels.items():
            with self.subTest(field=field):
                current_label = self.exercise._meta.get_field(field).verbose_name
                self.assertEqual(current_label, expected_label)

    def test__fields_max_length(self):
        """Testing max_length on the fields that have it"""

        max_lengths = {
            'name': 50,
            'muscle_group': 11,
            'equipment': 12,
        }

        for field, max_length in max_lengths.items():
            with self.subTest(field=field):
                current_max_length = self.exercise._meta.get_field(field).max_length
                self.assertEqual(current_max_length, max_length)
    
    def test__exercise_equipment_and_muscle_group_field_choices(self):
        field_choices = {
            'equipment': [
                ('dumbbell', 'Dumbbell'),
                ('bodyweight', 'Bodyweight'),
                ('barbell', 'Barbell'),
                ('cable', 'Cable'),
                ('e-z curl bar', 'E Z Curl Bar'),
                ('machine', 'Machine'),
                ('bands', 'Bands'),
                ('other', 'Other')],
            'muscle_group': [
                ('abdominals', 'Abdominals'),
                ('abductors', 'Abductors'),
                ('biceps', 'Biceps'),
                ('calves', 'Calves'),
                ('chest', 'Chest'),
                ('forearms', 'Forearms'),
                ('glutes', 'Glutes'),
                ('hamstrings', 'Hamstrings'),
                ('lats', 'Lats'),
                ('lower back', 'Lower Back'),
                ('middle back', 'Middle Back'),
                ('neck', 'Neck'),
                ('quadriceps', 'Quadriceps'),
                ('traps', 'Traps'),
                ('triceps', 'Triceps'),
                ('other', 'Other')]
        }

        for field, choices in field_choices.items():
            with self.subTest(field=field):
                current_choices = self.exercise._meta.get_field(field).choices
                self.assertEqual(current_choices, choices)
    
    def test__str(self):
        expected_output = self.exercise.name

        self.assertEqual(str(self.exercise), expected_output)