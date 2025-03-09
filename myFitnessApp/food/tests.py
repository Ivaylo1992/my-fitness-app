from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from myFitnessApp.utils.factory import AdminFactory, UserFactory


class USDAFoodSearchTest(APITestCase):
    def setUp(self):
        self.url = reverse('search_food')
        user = AdminFactory()
        self.client.force_authenticate(user=user)
        
    
    def test_search_with_bad_query__returns_400_bad_request(self):
        """Test API returns 400 if the query results in no data."""

        query = 'asdsdasdasdasd' # A query that should return no results
        expected_message = 'Failed to fetch data from USDA'

        response = self.client.get(query_params={'food_name': query}, path=self.url, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get('error'), expected_message)
    
    def test_search_with_empty_query__returns_400_bad_request(self):
        """Test API returns 400 if the query parameter is missing."""

        response = self.client.get(self.url, {'food_name': ''}, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get('error'), 'Query parameter is required')
    
    def test_search_with_valid_food_name__returns_200_OK(self):
        """Test API returns 200 and results when a valid food name is provided."""

        response = self.client.get(self.url, {'food_name': 'pork'}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)
        self.assertTrue(len(response.data.get('results', [])) > 0)


