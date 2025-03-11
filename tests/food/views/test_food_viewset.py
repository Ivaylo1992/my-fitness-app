from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from myFitnessApp.utils.factories import FoodFactory, UserFactory


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