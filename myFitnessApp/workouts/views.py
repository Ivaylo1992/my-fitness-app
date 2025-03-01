from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from myFitnessApp.workouts.models import Exercise
from myFitnessApp.workouts.serializers import ExerciseSerializer


class ExerciseListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()

    permission_classes = [IsAuthenticatedOrReadOnly]