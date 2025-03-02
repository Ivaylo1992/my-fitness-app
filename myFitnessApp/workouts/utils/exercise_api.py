import requests
from django.conf import settings
from rest_framework import status


API_BASE = 'https://api.api-ninjas.com/v1/exercises'


def search_exercise(query):
    
    API_KEY = settings.API_NINJAS_API_KEY

    headers = {
        "X-Api-Key": API_KEY
    }

    params = {
        "muscle": query,
        "page_size": 5,
    }
    
    response = requests.get(API_BASE, headers=headers, params=params)

    if response.status_code == status.HTTP_200_OK:
        return response.json()
    
    return []
