from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import AdminUser
from .serializers import (
    AdminUserCreateSerializer,
    AdminUserListSerializer,
)

# 🔐 ONLY MASTER ADMIN CAN MANAGE USERS
class IsMasterAdmin(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_superuser


class AdminUserCreateAPIView(APIView):
    permission_classes = [IsMasterAdmin]

    def post(self, request):
        serializer = AdminUserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        admin_user = serializer.save()

        return Response(
            {"message": "User created successfully"},
            status=status.HTTP_201_CREATED
        )


class AdminUserListAPIView(APIView):
    permission_classes = [IsMasterAdmin]

    def get(self, request):
        users = AdminUser.objects.all().order_by("-created_at")
        serializer = AdminUserListSerializer(users, many=True)
        return Response(serializer.data)
