from rest_framework.test import APITestCase
from myFitnessApp.workouts.models import Exercise
from myFitnessApp.workouts.serializers import WorkoutLogSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class TestWorkoutLogSerializer(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@example.com")
        self.client.force_authenticate(user=self.user)
        self.serializer = WorkoutLogSerializer
        self.exercise = Exercise.objects.create(name='test name', muscle_group='biceps')
    
    def test__create_method_with_workout_without_exercise_logs(self):
        data = {
            'name': 'Test Workout',
            'exercise_logs': [],
        }

        serializer = self.serializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)

        instance = serializer.save(user=self.user)
        
        self.assertEqual(instance.name, data['name'])
        self.assertTrue(len(instance.exercise_logs.all()) == 0)

    def test__create_method_with_workout_and_exercise_logs(self):
        data = {
                "name": "Test workout",
                "exercise_logs": [
                {
                    "id": 1,
                    "exercise": 1,
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

        self.assertTrue(len(instance.exercise_logs.all()) == 1)
        



        