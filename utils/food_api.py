import requests
from django.conf import settings
from rest_framework import status

USDA_API_BASE = 'https://api.nal.usda.gov/fdc/v1/foods/search'

def search_food(query):
    """
    Search food information in USDA FooData Central API

    """

    api_key = settings.USDA_API_KEY

    params = {
        'query': query,
        'api_key': api_key,
        'page_size': 5,
    }

    response = requests.get(USDA_API_BASE, params=params)

    if response.status_code == status.HTTP_200_OK:
        data = response.json()
       
        if 'foods' in data:
            return data['foods']
        return []
    return None
