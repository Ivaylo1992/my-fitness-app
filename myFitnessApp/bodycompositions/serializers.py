from rest_framework import serializers

from myFitnessApp.bodycompositions.models import BodyCompositionLog


class BodyCompositionLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyCompositionLog
        fields = ('weight', 'body_fat', 'user')
        read_only_fields = ('user', )
    
