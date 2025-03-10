from django.urls import path
from myFitnessApp.food import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'food', views.FoodViewSet, basename="food")
router.register(r'food_log', views.FoodLogViewSet, basename='food_log')


urlpatterns = [
    path("search/", views.SearchFoodAPIView.as_view(), name="search_food"),
] + router.urls