from django.urls import path
from myFitnessApp.food import views

urlpatterns = [
    path('search/', views.SearchFoodAPIView.as_view(), name='search_food'),
]