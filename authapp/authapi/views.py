from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignUpSerializer, LogInSerializer

# Create your views here.


@api_view(["POST"])
def signupRes(request):
    serializer = SignUpSerializer(data=request.data)
    if serializer.is_valid():
        if User.objects.filter(username=serializer.data["username"]).exists():
            return Response({"message": "Username is taken!"}, status=status.HTTP_401_UNAUTHORIZED)
        elif User.objects.filter(email=serializer.data["email"]).exists():
            return Response({"message": "Email is taken!"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            user = User.objects.create_user(username=serializer.data["username"], email=serializer.data["email"], password=serializer.data["password"])
            user.save()
            return Response({"message": "Succesfully signed up!"}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Validation Error!"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def loginRes(request):
    serializer = LogInSerializer(data=request.data)
    if serializer.is_valid():
        user = authenticate(request, username=serializer.data["username"], password=serializer.data["password"])
        if user is not None:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response({"message": "Username or password not correct!"}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({"message": "Validation Error!"}, status=status.HTTP_400_BAD_REQUEST)
