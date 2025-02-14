from django.urls import path
from myFitnessApp.accounts import views

urlpatterns = [
    path('signup/', views.SignupAPIView.as_view(), name='signup'),
]
