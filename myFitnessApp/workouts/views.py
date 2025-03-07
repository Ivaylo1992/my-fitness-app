from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes
from rest_framework.viewsets import ModelViewSet

from myFitnessApp.workouts.models import Exercise, WorkoutLog
from myFitnessApp.workouts.serializers import ExerciseSerializer, WorkoutLogSerializer
from myFitnessApp.workouts.utils.exercise_api import search_exercise


@extend_schema(
    tags=["exercises search"],
    summary="Search exercises endpoint",
    description="Search exercises from API ninjas.",
    parameters=[
        OpenApiParameter(
            name='muscle',
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
        )
    ]
)
class SearchExercisesAPIView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request):
        query = self.request.GET.get('muscle', '')

        if not query:
            return Response({
                'error': 'Query parameter is required'
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

        results = search_exercise(query=query)

        return Response(
            data=results,
            status=status.HTTP_200_OK
        )


@extend_schema(
    tags=["exercises"],
    summary="Exercises endpoint",
    description="All CRUD operations for the Exercise model.",
)
class ExerciseViewSet(ModelViewSet):
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()

    permission_classes = (IsAuthenticatedOrReadOnly, )


@extend_schema(
    tags=["workouts"],
    summary="Workout endpoint",
    description="All CRUD operations for the WorkoutLog model.",
)
class WorkoutViewSet(ModelViewSet):
    serializer_class = WorkoutLogSerializer
    queryset = WorkoutLog.objects.all()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)