from rest_framework import serializers

from django.contrib.auth import get_user_model

from myFitnessApp.accounts.models import FitnessAppProfile


UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ("email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = UserModel(
            email=validated_data["email"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user


class LoginRequestSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()


class LoginResponseSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()
    message = serializers.CharField()


class LogoutRequestSerializer(serializers.Serializer):
    refresh = serializers.CharField()


class LogoutResponseSerializer(serializers.Serializer):
    message = serializers.CharField()


class FitnessAppProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessAppProfile
        fields = ('first_name', 'last_name', 'date_of_birth',
                   'weight', 'height', 'profile_picture')