from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.request import Request
from django.contrib.auth import authenticate
from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

from myFitnessApp.accounts.models import FitnessAppProfile
from myFitnessApp.accounts.serializers import (
    FitnessAppProfileSerializer,
    LoginRequestSerializer,
    LoginResponseSerializer,
    LogoutRequestSerializer,
    LogoutResponseSerializer,
    UserSerializer,
)
from myFitnessApp.accounts.tokens import get_tokens_for_user

@extend_schema(
    tags=["auth"],
    summary="Signup endpoint",
    description="Endpoint for creating a new user.",
)
class SignupAPIView(generics.GenericAPIView):
    serializer_class = UserSerializer

    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    tags=["auth"],
    summary="Login endpoint",
    description="Authenticate a user and get back access and refresh tokens.",
    request=LoginRequestSerializer,
    responses={200: LoginResponseSerializer, 401: "Invalid email or password"},
)
class LoginAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)

        if user is not None:
            tokens = get_tokens_for_user(user)

            response = {"message": "Login successful", "tokens": tokens}

            return Response(response, status=status.HTTP_200_OK)

        return Response(data={"message": "Invalid email or password"})

    def get(self, request: Request):
        content = {"user": str(request.user), "auth": str(request.auth)}

        return Response(data=content, status=status.HTTP_200_OK)


@extend_schema(
    tags=["auth"],
    summary="Logout endpoint",
    description="Blacklist the refresh token",
    request=LogoutRequestSerializer,
    responses={200: LogoutResponseSerializer, 400: "Invalid or expired token"},
)
class LogoutAPIView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)

            return Response(
                {
                    "message": "Logout successful",
                },
                status=status.HTTP_200_OK,
            )

        except TokenError:
            return Response(
                {"error": "Invalid or expired token"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class ProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = FitnessAppProfileSerializer
    queryset = FitnessAppProfile.objects.all()

    def get_object(self):
        return get_object_or_404(FitnessAppProfile, pk=self.request.user.pk)
    
    @extend_schema(
        tags=['profile'],
        summary="Retrieve the profile of the request user",
        description="Fetch details of a specific profile by the request user.",
        responses={200: FitnessAppProfileSerializer}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @extend_schema(
        tags=['profile'],
        summary="Partially update the profile of the request user",
        description="Partially update a specific profile by the request user.",
        responses={200: FitnessAppProfileSerializer}
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    
    @extend_schema(
        tags=['profile'],
        summary="Update the profile of the request user",
        description="Update a specific profile by the request user.",
        responses={200: FitnessAppProfileSerializer}
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    