from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
import uuid


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10)

    role = models.CharField(max_length=100)

    organization = models.ForeignKey(
        "organization_management.Organization",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    branch = models.ForeignKey(
        "organization_management.Branch",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    employee_id = models.CharField(max_length=50, blank=True, null=True)
    approval_limit = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email
