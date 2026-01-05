from django.contrib import admin
from .models import ApprovalMaster, ApprovalAssignment, EscalationMaster


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





# ===============================
# MANAGE APPROVAL ADMIN
# ===============================
@admin.register(ApprovalAssignment)
class ApprovalAssignmentAdmin(admin.ModelAdmin):
    list_display = ("tenant_id", "user_or_group", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("tenant_id", "user_or_group")
    readonly_fields = ("created_at",)


# ===============================
# ESCALATION MASTER ADMIN
# ===============================
@admin.register(EscalationMaster)
class EscalationMasterAdmin(admin.ModelAdmin):
    list_display = (
        "escalation_level",
        "escalation_time",
        "escalation_manager",
        "escalation_to",
        "status",
        "created_at",
    )
    list_filter = ("escalation_level", "status")
    readonly_fields = ("created_at",)
