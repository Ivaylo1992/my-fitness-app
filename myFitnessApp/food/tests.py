from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class USDAFoodSearchTest(APITestCase):
    def setUp(self):
        self.url = reverse('search_food')
    
    def test_search_with_bad_query__returns_400_bad_request(self):
        query = 'asdsdasdasdasd' # query that gives no results
        expected_message = 'Failed to fetch data from USDA'

        response = self.client.get(query_params={'food_name': query}, path=self.url, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get('error'), expected_message)
    
    def test_search_with_empty_query__returns_400_bad_request(self):
        query = ''
        expected_message = 'Query parameter is required'

        response = self.client.get(query_params={'food_name': query}, path=self.url, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get('error'), expected_message)
    
    def test_search_with_valid_food_name__returns_200_OK(self):
        query = 'pork'

        response = self.client.get(query_params={'food_name': query}, path=self.url, format='json')

        self.assertTrue(response.data.get('count') > 0)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


