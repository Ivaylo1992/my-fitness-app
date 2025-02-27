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
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes


@extend_schema(
    tags=["food"],
    summary="Search food endpoint",
    description="Search food from USDA API.",
    parameters=[
        OpenApiParameter(
            name='food_name',
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
        )
    ]
)
class SearchFoodAPIView(APIView):
    def get(self, request):
        query = self.request.GET.get("food_name", "")
        if not query:
            return Response(
                {"error": "Query parameter is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        food_data = search_food(query=query)
        if not food_data:
            response = {"error": "Failed to fetch data from USDA"}

            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        results = get_food_data(food_data)

        paginator = PageNumberPagination()
        paginated_results = paginator.paginate_queryset(results, request)
        return paginator.get_paginated_response(paginated_results)


@extend_schema(
    tags=["food"],
    summary="Food endpoint",
    description="All CRUD operations for the food model.",
)
class FoodViewSet(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


@extend_schema(
    tags=["food log"],
    summary="Food log list create endpoint",
    description="Creates a food log and list already created logs",
)
class FoodLogListCreate(generics.ListCreateAPIView):
    serializer_class = FoodLogSerializer
    queryset = FoodLog.objects.all()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


@extend_schema(
    tags=["food log"],
    summary="Food log retrieve update endpoint",
    description="Deletes , updates or retrieves a food log by ID",
)
class FoodLogRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FoodLogSerializer
    queryset = FoodLog.objects.all()
