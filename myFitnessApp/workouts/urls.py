from django.urls import path
from myFitnessApp.workouts import views

urlpatterns = [
    path('search/', views.SearchExercisesAPIView.as_view(), name='search_exercises_api'),
    path('exercises/', views.ExerciseListCreateAPIView.as_view(), name='exercises_list_create'),
    path('exercises/<int:pk>', views.ExerciseRetrieveUpdateDeleteAPIView.as_view(), name='exercises_retrieve_update_delete'),
    path('workout_log/', views.WorkoutLogCreateAPIView.as_view(), name='workout_log_create'),
]
