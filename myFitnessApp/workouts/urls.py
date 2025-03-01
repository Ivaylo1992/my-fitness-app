from django.urls import path
from myFitnessApp.workouts import views

urlpatterns = [
    path('exercises/', views.ExerciseListCreateAPIView.as_view(), name='exercises list create'),
]
