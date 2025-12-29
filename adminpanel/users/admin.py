from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "phone_number",
        "role",
        "organization",
        "branch",
        "is_active",
        "created_at",
    )
    search_fields = ("email", "phone_number", "employee_id")
    list_filter = ("role", "is_active")
    ordering = ("-created_at",)
