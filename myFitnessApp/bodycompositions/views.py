from rest_framework.viewsets import ModelViewSet

from myFitnessApp.bodycompositions.models import BodyCompositionLog, BodyMeasurements
from myFitnessApp.bodycompositions.serializers import BodyCompositionLogSerializer, BodyMeasurementsSerializer

class BodyCompositionLogViewSet(ModelViewSet):
    serializer_class = BodyCompositionLogSerializer
    queryset = BodyCompositionLog.objects.all()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class BodyMeasurementsLogViewSet(ModelViewSet):
    serializer_class = BodyMeasurementsSerializer
    queryset = BodyMeasurements.objects.all()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
