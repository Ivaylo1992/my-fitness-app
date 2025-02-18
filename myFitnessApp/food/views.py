from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response
from myFitnessApp.food.models import Food
from myFitnessApp.food.serializers import FoodSerializer
from utils.food_data import get_food_data
from utils.food_api import search_food
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet



class SearchFoodAPIView(APIView):
    @swagger_auto_schema(
        operation_summary = 'Search food data from USDA Food API',
        operation_description='Search food data from USDA Food API',
        manual_parameters=[
            openapi.Parameter(
                'query', 
                openapi.IN_QUERY,
                description="Search term for food items",
                type=openapi.TYPE_STRING,
                required=True
            )
        ]
    )
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

        paginator = PageNumberPagination()
        paginated_results = paginator.paginate_queryset(results, request)
        return paginator.get_paginated_response(paginated_results)



class FoodViewSet(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer