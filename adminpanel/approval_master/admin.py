from django.contrib import admin
from .models import ApprovalMaster


@admin.register(ApprovalMaster)
class ApprovalMasterAdmin(admin.ModelAdmin):
    list_display = (
        "level",
        "type",
        "product_type",
        "product_name",
        "sanction_name",
        "status",
        "created_at",
    )

    list_filter = ("level", "type", "status", "product_type")
    search_fields = ("product_name", "sanction_name")
    readonly_fields = ("created_at",)


