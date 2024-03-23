from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from .models import User
# Create your views here.


class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            user = User.objects.get(username=request.data.get('username'))
        except Exception:
            return Response({"error": {"message": "Your username and password didn't match"}}, status=status.HTTP_401_UNAUTHORIZED)

        auth_user = authenticate(request, username=user.username, password=request.data.get('password'))
        if auth_user:
            login(request, auth_user)
            return Response({"status": True, "username": auth_user.username, "user_id": request.user.id}, status=status.HTTP_200_OK,)
        return Response({"error": {"message": "Your username and password didn't match. Please try again"}}, status=status.HTTP_401_UNAUTHORIZED)


class IsUserLoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        if request.user.is_authenticated:
            return Response({"status": True, "username": request.user.username, "user_id": request.user.id}, status=status.HTTP_200_OK)
        return Response({"status": False}, status=status.HTTP_401_UNAUTHORIZED)


class UserLogoutView(APIView):

    def get(self, request):
        logout(request)
        return Response({"message": "User logged out successfully."}, status=status.HTTP_200_OK)
