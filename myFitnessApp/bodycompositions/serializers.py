from rest_framework import serializers

from myFitnessApp.bodycompositions.models import BodyCompositionLog, BodyMeasurements


class BodyCompositionLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyCompositionLog
        fields = ('weight', 'body_fat', 'user')
        read_only_fields = ('user', )
    

class BodyMeasurementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyMeasurements
        fields = ('neck', 'chest', 'biceps', 'waist', 'hips', 'thigh', 'calf', 'user')
        read_only_fields = ('user', )