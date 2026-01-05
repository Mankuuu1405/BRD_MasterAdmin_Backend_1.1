from rest_framework import serializers
from django.contrib.auth.models import Group
from auth_service.accounts.models import User
from .models import AdminUser


class AdminUserCreateSerializer(serializers.Serializer):
    # User fields
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(required=False, allow_blank=True)

    # RBAC
    role_id = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(),
        source="role"
    )

    # Business fields
    organization = serializers.CharField(required=False, allow_blank=True)
    branch = serializers.CharField(required=False, allow_blank=True)
    employee_id = serializers.CharField(required=False, allow_blank=True)
    approval_limit = serializers.DecimalField(
        max_digits=15, decimal_places=2, required=False
    )

    def create(self, validated_data):
        # Extract role
        role = validated_data.pop("role")

        # Create AUTH user
        user = User.objects.create_user(
            email=validated_data.pop("email"),
            password=validated_data.pop("password")
        )

        # Create ADMIN user
        admin_user = AdminUser.objects.create(
            user=user,
            role=role,
            **validated_data
        )

        return admin_user
    
class AdminUserListSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source="user.email")
    role = serializers.CharField(source="role.name", default=None)

    class Meta:
        model = AdminUser
        fields = [
            "id",
            "email",
            "phone_number",
            "role",
            "employee_id",
            "approval_limit",
            "is_active",
            "created_at",
        ] 
