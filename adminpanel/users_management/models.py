from django.db import models
from auth_service.accounts.models import User
import uuid


class AdminUser(models.Model):
    """
    Business user for Master Admin panel
    This maps exactly to the 'Add User' frontend screen
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="admin_profile"
    )

    organization = models.CharField(max_length=150)
    branch = models.CharField(max_length=150, null=True, blank=True)

    employee_id = models.CharField(max_length=50, null=True, blank=True)
    approval_limit = models.DecimalField(
        max_digits=15, decimal_places=2, null=True, blank=True
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Admin User"
        verbose_name_plural = "Admin Users"

    def __str__(self):
        return self.user.email
