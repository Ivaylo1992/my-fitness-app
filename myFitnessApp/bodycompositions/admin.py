from django.contrib import admin

from myFitnessApp.bodycompositions.models import BodyCompositionLog, BodyMeasurements

@admin.register(BodyCompositionLog)
class BodyCompositionLogAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', 'created_at', 'user')


@admin.register(BodyMeasurements)
class BodyMeasurementsAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', 'created_at', 'user')
