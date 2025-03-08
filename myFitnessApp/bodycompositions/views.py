from rest_framework.viewsets import ModelViewSet

from myFitnessApp.bodycompositions.models import BodyCompositionLog
from myFitnessApp.bodycompositions.serializers import BodyCompositionLogSerializer

class BodyCompositionLogViewSet(ModelViewSet):
    serializer_class = BodyCompositionLogSerializer
    queryset = BodyCompositionLog.objects.all()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

