from django.urls import path
from myFitnessApp.food import views

urlpatterns = [
    path('search/', views.SearchFoodAPIView.as_view(), name='search_food'),
    path('', views.FoodAPIView.as_view(), name='food_list_create'),
]