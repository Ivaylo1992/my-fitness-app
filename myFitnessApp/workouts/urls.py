from django.urls import path
from myFitnessApp.workouts import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'exercises', views.ExerciseViewSet, basename="exercises")
router.register(r'workouts', views.WorkoutViewSet, basename="workouts")

urlpatterns = [
    path('search/', views.SearchExercisesAPIView.as_view(), name='search_exercises_api'),    
] + router.urls
