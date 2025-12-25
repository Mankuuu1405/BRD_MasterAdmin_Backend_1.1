from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LoginSerializer


class LoginView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        user = authenticate(
            request=request,      # 🔴 REQUIRED BY AXES
            username=email,       # 🔴 MUST BE username
            password=password
        )

        if not user or not user.is_master_admin:
            return Response(
                {"error": "Invalid master admin credentials"},
                status=401
            )

        refresh = RefreshToken.for_user(user)

        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "role": "MASTER_ADMIN"
        })
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LoginSerializer


class LoginView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        user = authenticate(
            request=request,      # ✅ REQUIRED for django-axes
            username=email,       # ✅ MUST be "username"
            password=password
        )

        if not user:
            return Response(
                {"error": "Invalid credentials"},
                status=401
            )

        # OPTIONAL: restrict only master admins
        # if not user.is_staff:
        if not user or not user.is_staff:
         return Response(
         {"error": "Unauthorized master admin"},
         status=403
            )

        #     return Response({"error": "Unauthorized"}, status=403)

        refresh = RefreshToken.for_user(user)

        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "role": "MASTER_ADMIN"
        })