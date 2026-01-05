from rest_framework import serializers
from auth_service.accounts.models import User
from .models import AdminUser


class AdminUserCreateSerializer(serializers.Serializer):
    """
    Used by frontend Add User screen
    """

    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    organization = serializers.CharField()
    branch = serializers.CharField(required=False, allow_blank=True)

    employee_id = serializers.CharField(required=False, allow_blank=True)
    approval_limit = serializers.DecimalField(
        max_digits=15, decimal_places=2, required=False
    )

    is_active = serializers.BooleanField(default=True)

    def create(self, validated_data):
        email = validated_data.pop("email")
        password = validated_data.pop("password")

        user = User.objects.create_user(
            email=email,
            password=password
        )

        admin_user = AdminUser.objects.create(
            user=user,
            **validated_data
        )

        return admin_user


class AdminUserListSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source="user.email")

    class Meta:
        model = AdminUser
        fields = [
            "id",
            "email",
            "organization",
            "branch",
            "employee_id",
            "approval_limit",
            "is_active",
            "created_at",
        ]
