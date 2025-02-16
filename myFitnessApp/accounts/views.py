from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.request import Request
from django.contrib.auth import authenticate

from myFitnessApp.accounts.serializers import UserSerializer
from myFitnessApp.accounts.tokens import get_tokens_for_user


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
    

class LoginAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request:Request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)

        if user is not None:
            tokens = get_tokens_for_user(user)

            response = {
                'message': 'Login successful',
                'tokens': tokens
            }

            return Response(response, status=status.HTTP_200_OK)
        
        return Response(data={"message": "Invalid email or password"})
    
    
    def get(self, request: Request):
        content = {'user': str(request.user), 'auth': str(request.auth)}

        return Response(data=content, status=status.HTTP_200_OK)


            