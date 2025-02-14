from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from myFitnessApp.accounts.serializers import UserSerializer


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
            