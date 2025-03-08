from django.urls import path
from rest_framework.routers import DefaultRouter
from myFitnessApp.bodycompositions import views

router = DefaultRouter()
router.register(r'weight_ins', views.BodyCompositionLogViewSet, basename='weight_ins')
router.register(r'body_measurements', views.BodyMeasurementsLogViewSet, basename='body_measurements')

urlpatterns = [
	
] + router.urls
