from django.urls import path
from myFitnessApp.accounts import views

urlpatterns = [
    path("signup/", views.SignupAPIView.as_view(), name="signup"),
    path("login/", views.LoginAPIView.as_view(), name="login"),
    path("logout/", views.LogoutAPIView.as_view(), name="logout"),
    path("profile/", views.ProfileRetrieveUpdateDestroyAPIView.as_view(), name="profile_retrieve_update_destroy"),
]


