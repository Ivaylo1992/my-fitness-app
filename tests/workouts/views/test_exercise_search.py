from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from myFitnessApp.utils.factories import UserFactory


class SearchExerciseTest(APITestCase):
    def setUp(self):
        self.url = reverse('search_exercises_api')
        user = UserFactory()
        self.client.force_authenticate(user=user)
    
    def test_get_without_query(self):
        response = self.client.get(self.url, {'muscle': ''}, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get('error'), 'Query parameter is required')
    
    def test_get__with_invalid_muscle_group(self):
        response = self.client.get(self.url, {'muscle': 'chicken'}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])
    
    def test_get__with_valid_muscle_group(self):
        response = self.client.get(self.url, {'muscle': 'biceps'}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('name', response.data[0])
        self.assertTrue(len(response.data) > 0)