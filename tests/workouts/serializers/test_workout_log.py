from rest_framework.test import APITestCase
from myFitnessApp.utils.factories import ExerciseFactory, UserModelFactory
from myFitnessApp.workouts.models import WorkoutLog
from myFitnessApp.workouts.serializers import WorkoutLogSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class TestWorkoutLogSerializer(APITestCase):
    def setUp(self):
        self.user = UserModelFactory()
        self.serializer = WorkoutLogSerializer
        self.exercise = ExerciseFactory()
    
    def test__create_method_with_workout_without_exercise_logs(self):
        data = {
            'name': 'Test Workout',
            'exercise_logs': [],
        }

        serializer = self.serializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        instance = serializer.save(user=self.user)

        self.assertEqual(instance.name, data['name'])
        self.assertEqual(instance.exercise_logs.count(), 0)

    def test__create_method_with_workout_and_exercise_logs(self):
        data = {
                "name": "Test workout",
                "exercise_logs": [
                {
                    "exercise": self.exercise.id,
                    "repetitions": 12,
                    "weight": 120,
                    "rest_time": 90,
                    "notes": "test note"
                }
            ]         
        }

        serializer = self.serializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        instance = serializer.save(user=self.user)

        self.assertEqual(instance.exercise_logs.count(), 1)
        self.assertEqual(instance.name, data["name"])
        self.assertIsNotNone(instance.id)

    
    def test__update_method_with_empty_workout(self):
        instance = WorkoutLog.objects.create(name='Test2', user=self.user)
        
        self.assertEqual(instance.exercise_logs.count(), 0)

        data = {
            'name': 'Test3',
            'exercise_logs': [
                {
                    "exercise": self.exercise.id,
                    "repetitions": 12,
                    "weight": 120,
                    "rest_time": 90,
                    "notes": "test note"
                },
                {
                    "exercise": self.exercise.id,
                    "repetitions": 11,
                    "weight": 110,
                    "rest_time": 80,
                    "notes": "test note"
                }
            ]
        }

        serializer = self.serializer(instance, data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        updated_instance = serializer.save()

        self.assertTrue(updated_instance.exercise_logs.count() == 2)
        self.assertEqual(updated_instance.name, data["name"])

    def test__update_method_partially(self):
        data = {
                "name": "Test workout",
                "exercise_logs": [
                {
                    "exercise": self.exercise.id,
                    "repetitions": 12,
                    "weight": 120,
                    "rest_time": 90,
                    "notes": "test note"
                }
            ]         
        }

        serializer = self.serializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        instance = serializer.save(user=self.user)

        new_data = {
            'exercise_logs': [
            {
                'id': instance.exercise_logs.first().pk,
                'notes': 'Edited notes'
            }
        ]}

        serializer = self.serializer(instance, data=new_data, partial=True)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        updated_instance = serializer.save()
        
        self.assertEqual(updated_instance.exercise_logs.get(
            pk=instance.exercise_logs.first().pk).notes, "Edited notes")