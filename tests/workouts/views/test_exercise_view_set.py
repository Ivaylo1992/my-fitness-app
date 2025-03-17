from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from myFitnessApp.utils.factories import ExerciseFactory, UserModelFactory
from tests.utils.mixins import RequestHelperMixin


class ExerciseViewSetTest(RequestHelperMixin, APITestCase):
    def setUp(self):
        self.user = UserModelFactory()
        self.client = APIClient()
        self.exercise = ExerciseFactory()
    
    def test__get_with_authenticated_and_unauthenticated_user_returns_200_ok(self):
        url = reverse('exercises-list')
        method = 'get'

        response = self.send_request(url=url, method=method)

        self.assertEqual(response.data.get('count'), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Authenticate the user and check if the response is the same 

        new_response = self.send_request(method=method, url=url, authenticate=True)

        self.assertEqual(new_response.data.get('count'), 1)
        self.assertEqual(new_response.status_code, status.HTTP_200_OK)

    def test__post_with_unauthenticated_user__returns_403_forbidden(self):
        data = {
            'name': 'Post Exercise',
            'muscle_group': 'chest',
            'equipment': 'barbell',
            'instructions': 'just do it!'
        }
        method = 'post'
        
        url = reverse('exercises-list')
        response = self.send_request(method=method, url=url, data=data)
        
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
        method = 'post'
        
        url = reverse('exercises-list')
        response = self.send_request(method=method, url=url, data=data, authenticate=True)
        print(response.data)

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
        method = 'get'

        response = self.send_request(method=method, url=url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

        # Authenticate the user and check if the response is the same 

        new_response = self.send_request(method=method, url=url, authenticate=True)

        self.assertEqual(new_response.status_code, status.HTTP_200_OK)
        self.assertEqual(new_response.data, expected_data)
    
    def test__get_exercise_with_invalid_pk__returns_404_not_found(self):
        url = reverse('exercises-detail', kwargs={'pk': 2})
        method = 'get'
        expected_message = 'No Exercise matches the given query.'

        response = self.send_request(method=method, url=url)

        self.assertEqual(response.data.get('detail'), expected_message)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test__put_with_unauthenticated_user__returns_403_forbidden(self):
        url = reverse('exercises-detail', kwargs={'pk': self.exercise.pk})

        data = {
            'name': 'Post Exercise',
            'muscle_group': 'biceps',
            'equipment': 'barbell',
            'instructions': 'just do it!'
        }
        method = 'put'

        response = self.send_request(method=method, url=url, data=data)

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
        method = 'put'

        response = self.send_request(method=method, url=url, data=data, authenticate=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for field, value in data.items():
            self.assertEqual(response.data[field], value)


    def test__patch_with_unauthenticated_user__returns_403_forbidden(self):
        url = reverse('exercises-detail', kwargs={'pk': self.exercise.pk})

        data = {
            'name': 'Patch Exercise',
        }
        method = 'patch'

        response = self.send_request(method=method, url=url, data=data)

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
        method = 'patch'

        response = self.send_request(method=method, url=url, data=data, authenticate=True)

        self.assertEqual(response.data.get('name'), data['name'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test__delete_with_unauthenticated_user__returns_403_forbidden(self):
        url = reverse('exercises-detail', kwargs={'pk': self.exercise.pk})
        method = 'delete'

        response = self.send_request(method=method, url=url)

        self.assertEqual(
            response.data.get('detail'),
            'Authentication credentials were not provided.'
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test__delete_with_authenticated_user__returns_204_no_content(self):
        url = reverse('exercises-detail', kwargs={'pk': self.exercise.pk})
        method = 'delete'

        response = self.send_request(method=method, url=url, authenticate=True)

        self.assertFalse(response.data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)