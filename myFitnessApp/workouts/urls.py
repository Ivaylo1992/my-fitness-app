from django.urls import path
from myFitnessApp.workouts import views

urlpatterns = [
    path('search/', views.SearchExercisesAPIView.as_view(), name='search_exercises_api'),
    path('exercises/', views.ExerciseListCreateAPIView.as_view(), name='exercises_list_create'),
]
