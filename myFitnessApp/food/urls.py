from django.urls import path
from myFitnessApp.food import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', views.FoodViewSet, basename='food')
# router.register(r'food_log', views.FoodLogViewSet, basename='food_log')


urlpatterns = [
    path('search/', views.SearchFoodAPIView.as_view(), name='search_food'),
    path('food_log/', views.FoodLogListCreate.as_view(), name='food_log_list_create'),
    path('food_log/<int:pk>/',
          views.FoodLogRetrieveUpdateDestroy.as_view(), name='food_log_retrieve_update_destroy'),
] + router.urls