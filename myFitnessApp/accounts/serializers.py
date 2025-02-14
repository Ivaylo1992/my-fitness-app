from rest_framework import serializers

from django.contrib.auth import get_user_model


UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    
    def create(self, validated_data):
        user = UserModel(
            email = validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user