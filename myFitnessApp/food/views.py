from rest_framework.views import APIView
from rest_framework.response import Response
from myFitnessApp.food.models import Food, FoodLog
from myFitnessApp.food.serializers import FoodLogSerializer, FoodSerializer
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes


from myFitnessApp.food.utils.food_api import search_food
from myFitnessApp.food.utils.food_data import get_food_data


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
    permission_classes = (IsAdminUser, )
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
    summary="Food log endpoint",
    description="All CRUD operations for the food log model.",
)
class FoodLogViewSet(ModelViewSet):
    queryset = FoodLog.objects.all()
    serializer_class = FoodLogSerializer
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
