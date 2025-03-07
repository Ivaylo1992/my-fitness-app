from django.contrib import admin

from myFitnessApp.bodycompositions.models import BodyCompositionLog, BodyMeasurements

@admin.register(BodyCompositionLog)
class BodyCompositionLogAdmin(admin.ModelAdmin):
    ...


@admin.register(BodyMeasurements)
class BodyMeasurementsAdmin(admin.ModelAdmin):
    ...
