from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from myFitnessApp.utils.factories import ExerciseFactory, UserModelFactory


class ExerciseViewSetTest(APITestCase):
    def setUp(self):
        self.user = UserModelFactory()
        self.client = APIClient()
        self.exercise = ExerciseFactory()
    
    def test__get_with_authenticated_and_unauthenticated_user_returns_200_ok(self):
        url = reverse('exercises-list')

        response = self.client.get(url)

        self.assertEqual(response.data.get('count'), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Authenticate the user and check if the response is the same 

        self.client.force_authenticate(user=self.user)

        response = self.client.get(url)

        self.assertEqual(response.data.get('count'), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test__post_with_unauthenticated_user__returns_403_forbidden(self):
        data = {
            'name': 'Post Exercise',
            'muscle_group': 'biceps',
            'equipment': 'barbell',
            'instructions': 'just do it!'
        }
        
        url = reverse('exercises-list')
        response = self.client.post(url, data=data)
        
        self.assertEqual(
            response.data.get('detail'),
            'Authentication credentials were not provided.'
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test__post_with_authenticated_user__returns_201_created(self):
        data = {
            'name': 'Post Exercise',
            'muscle_group': 'biceps',
            'equipment': 'barbell',
            'instructions': 'just do it!'
        }
        
        self.client.force_authenticate(user=self.user)
        url = reverse('exercises-list')
        response = self.client.post(url, data=data)

        self.assertEqual(response.data.get('name'), 'Post Exercise')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    

    def test__get_exercise_with_authenticated_and_unauthenticated_user_returns_200_ok(self):
        url = reverse('exercises-detail', kwargs={'pk': self.exercise.pk})

        expected_data = {
            'name': self.exercise.name,
            'muscle_group': self.exercise.muscle_group,
            'equipment': self.exercise.equipment,
            'exercise_picture': self.exercise.exercise_picture,
            'exercise_video': self.exercise.exercise_video,
            'instructions': self.exercise.instructions
        }

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

        # Authenticate the user and check if the response is the same 

        self.client.force_authenticate(user=self.user)

        new_response = self.client.get(url)

        self.assertEqual(new_response.status_code, status.HTTP_200_OK)
        self.assertEqual(new_response.data, expected_data)

    def test__put_with_unauthenticated_user__returns_403_forbidden(self):
        url = reverse('exercises-detail', kwargs={'pk': self.exercise.pk})

        data = {
            'name': 'Post Exercise',
            'muscle_group': 'biceps',
            'equipment': 'barbell',
            'instructions': 'just do it!'
        }

        response = self.client.put(url, data)

        self.assertEqual(
            response.data.get('detail'),
            'Authentication credentials were not provided.'
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test__put_with_authenticated_user__returns_200_ok(self):
        url = reverse('exercises-detail', kwargs={'pk': self.exercise.pk})

        data = {
            'name': 'Put Exercise Edit',
            'muscle_group': 'chest',
            'equipment': 'dumbbell',
            'instructions': 'just do it edit'
        }

        self.client.force_authenticate(user=self.user)

        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for field, value in data.items():
            self.assertEqual(response.data[field], value)


    def test__patch_with_unauthenticated_user__returns_403_forbidden(self):
        url = reverse('exercises-detail', kwargs={'pk': self.exercise.pk})

        data = {
            'name': 'Patch Exercise',
        }

        response = self.client.patch(url, data)

        self.assertEqual(
            response.data.get('detail'),
            'Authentication credentials were not provided.'
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    
    def test__patch_with_authenticated_user__returns_200_ok(self):
        url = reverse('exercises-detail', kwargs={'pk': self.exercise.pk})
    
        data = {
            'name': 'Patch Exercise Edit',
        }

        self.client.force_authenticate(user=self.user)

        response = self.client.patch(url, data)

        self.assertEqual(response.data.get('name'), data['name'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)