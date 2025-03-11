import json
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from myFitnessApp.utils.factories import AdminFactory, FoodFactory, UserFactory


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


class FoodViewSetTest(APITestCase):
    def setUp(self):
        self.food = FoodFactory()
        user = UserFactory()
        self.client.force_authenticate(user=user)
        
    def test_get_request(self):
        url = reverse('food-list')
        response = self.client.get(url)
        response.render()

        expected_content = [{
            'food_name' : self.food.food_name,
            'protein': self.food.protein,
            'carbohydrates': self.food.carbohydrates,
            'fats': self.food.fats,
            'serving_size': self.food.serving_size,
            'serving_size_unit': self.food.serving_size_unit,
            'calories': self.food.calories
        }]

        self.assertEqual(response.data.get('results'), expected_content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    