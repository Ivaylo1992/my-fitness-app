from django.urls import path
from rest_framework.routers import DefaultRouter
from myFitnessApp.bodycompositions import views

router = DefaultRouter()
router.register(r'weight_ins', views.BodyCompositionLogViewSet, basename='weight_ins' )

urlpatterns = [
	
] + router.urls
