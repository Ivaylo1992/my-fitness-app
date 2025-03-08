from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema

from myFitnessApp.bodycompositions.models import BodyCompositionLog, BodyMeasurements
from myFitnessApp.bodycompositions.serializers import BodyCompositionLogSerializer, BodyMeasurementsSerializer

@extend_schema(
    tags=["weight ins"],
    summary="Weight in endpoint",
    description="All CRUD operations for the BodyCompositionLog model.",
)
class BodyCompositionLogViewSet(ModelViewSet):
    serializer_class = BodyCompositionLogSerializer
    queryset = BodyCompositionLog.objects.all()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


@extend_schema(
    tags=["body measurements"],
    summary="Body Measurements endpoint",
    description="All CRUD operations for the BodyMeasurements model.",
)
class BodyMeasurementsLogViewSet(ModelViewSet):
    serializer_class = BodyMeasurementsSerializer
    queryset = BodyMeasurements.objects.all()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
