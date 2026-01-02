from django.contrib import admin
from .models import AdminUser


@admin.register(AdminUser)
class AdminUserAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "organization",
        "branch",
        "employee_id",
        "approval_limit",
        "is_active",
        "created_at",
    )

    list_filter = ("is_active", "organization")
    search_fields = ("user__email", "employee_id")
    readonly_fields = ("created_at",)
