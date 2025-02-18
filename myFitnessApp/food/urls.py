from django.urls import path
from myFitnessApp.food import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', views.FoodViewSet, basename='food')


urlpatterns = [
    path('search/', views.SearchFoodAPIView.as_view(), name='search_food'),
] + router.urls