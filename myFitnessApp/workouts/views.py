from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes

from myFitnessApp.workouts.models import Exercise
from myFitnessApp.workouts.serializers import ExerciseSerializer
from myFitnessApp.workouts.utils.exercise_api import search_exercise


@extend_schema(
    tags=["exercises"],
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



class ExerciseListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()

    permission_classes = (IsAuthenticatedOrReadOnly, )


class ExerciseRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()
    
    permission_classes = (IsAuthenticatedOrReadOnly, )

