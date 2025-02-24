from rest_framework.views import APIView
from rest_framework.response import Response
from myFitnessApp.food.models import Food, FoodLog
from myFitnessApp.food.serializers import FoodLogSerializer, FoodSerializer
from utils.food_data import get_food_data
from utils.food_api import search_food
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet


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

        paginator = PageNumberPagination()
        paginated_results = paginator.paginate_queryset(results, request)
        return paginator.get_paginated_response(paginated_results)


class FoodViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Food.objects.all().prefetch_related('logs')
    serializer_class = FoodSerializer


class FoodLogListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FoodLogSerializer
    queryset = FoodLog.objects.all()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class FoodLogRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FoodLogSerializer
    queryset = FoodLog.objects.all()