from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Role, Permission, RolePermission, UserRole
from .serializers import (
    RoleSerializer,
    PermissionSerializer,
    RolePermissionSerializer,
    UserRoleSerializer,
)


# ---------- ROLES ----------
class RoleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]


# ---------- PERMISSIONS ----------
class PermissionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [IsAuthenticated]


# ---------- ASSIGN PERMISSION TO ROLE ----------
class AssignPermissionToRoleAPIView(generics.CreateAPIView):
    queryset = RolePermission.objects.all()
    serializer_class = RolePermissionSerializer
    permission_classes = [IsAuthenticated]


# ---------- ASSIGN ROLE TO USER ----------
class AssignRoleToUserAPIView(generics.CreateAPIView):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer
    permission_classes = [IsAuthenticated]


# ---------- USER ROLES LIST ----------
class UserRoleListAPIView(generics.ListAPIView):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer
    permission_classes = [IsAuthenticated]
