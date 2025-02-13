from rest_framework.views import APIView
from rest_framework.response import Response
from utils.food_data import get_food_data
from utils.food_api import search_food
from rest_framework import status


class SearchFoodAPIView(APIView):
    def get(self, request):
        query = self.request.GET.get('query', '')
        if not query:
            return Response({"error": "Query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

        food_data = search_food(query=query)
        if not food_data:
            response = {
                "error": "Failed to fetch data from USDA"
            }

            return Response(response, status=status.HTTP_400_BAD_REQUEST)


        results = get_food_data(food_data)

        return Response(results,status=status.HTTP_200_OK)



