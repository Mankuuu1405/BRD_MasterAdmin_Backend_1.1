from django.contrib import admin

# ================= ACCESS CONTROL =================
from adminpanel.access_control.models import Role


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "created_at")
    readonly_fields = ("created_at",)


# ================= APPROVAL MASTER =================
from adminpanel.approval_master.models import ApprovalMaster


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


# ================= PRODUCT MANAGEMENT =================
from adminpanel.product_management.models import LoanProduct, ProductFacility


@admin.register(ProductFacility)
class ProductFacilityAdmin(admin.ModelAdmin):
    list_display = (
        "facility_name",
        "loan_product",
        "is_mandatory",
        "is_active",
        "created_at",
    )
    readonly_fields = ("created_at",)


@admin.register(LoanProduct)
class LoanProductAdmin(admin.ModelAdmin):
    list_display = (
        "product_name",
        "product_category",
        "product_type",
        "product_amount",
        "product_period_value",
        "product_period_unit",
        "is_active",
        "created_at",
    )
    readonly_fields = ("created_at",)
    list_filter = ("product_category", "product_type", "is_active")
    search_fields = ("product_name", "product_category", "product_type")


# ================= PRODUCT MIX =================
from adminpanel.product_mix_management.models import ProductMix


@admin.register(ProductMix)
class ProductMixAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "product_category",
        "product_type",
        "is_active",
        "created_at",
    )
    filter_horizontal = ("products",)
    readonly_fields = ("created_at",)


# ================= ELIGIBILITY & SCORE MANAGEMENT =================
from adminpanel.eligibility_score_management.models import (
    EligibilityManagement,
    BankingManagement,
    ExistingObligationManagement,
    ScoreCardManagement,
)


@admin.register(EligibilityManagement)
class EligibilityManagementAdmin(admin.ModelAdmin):
    list_display = (
        "applicant_type",
        "category",
        "income_type",
        "is_active",
        "created_at",
    )
    readonly_fields = ("created_at",)


@admin.register(BankingManagement)
class BankingManagementAdmin(admin.ModelAdmin):
    list_display = (
        "bank_account_type",
        "average_banking_criteria",
        "is_active",
        "created_at",
    )
    readonly_fields = ("created_at",)


@admin.register(ExistingObligationManagement)
class ExistingObligationManagementAdmin(admin.ModelAdmin):
    list_display = (
        "loan_status",
        "loan_performance",
        "total_loans",
        "is_active",
        "created_at",
    )
    readonly_fields = ("created_at",)


@admin.register(ScoreCardManagement)
class ScoreCardManagementAdmin(admin.ModelAdmin):
    list_display = (
        "impact_type",
        "risk_impact",
        "is_active",
        "created_at",
    )
    readonly_fields = ("created_at",)


# ================= RISK & MITIGATION MANAGEMENT =================
# IMPORTANT: importing admin auto-registers all 8 models
import adminpanel.risk_mitigation_management.admin

# ================= MIS & REPORTING =================
import adminpanel.mis_reporting_management.admin

# ================= system settings =================
import adminpanel.system_settings.admin 

# ================= subscription management =================
import adminpanel.subscription_management.admin

# ================= coupon management =================
import adminpanel.coupon_management.admin

# ================= bank funds management =================
import adminpanel.bank_funds_management.admin

# ================= profile management =================
import adminpanel.profile_management.admin

# ================= agent management =================
import adminpanel.agent_management.admin

# ================= rule management =================
import adminpanel.rule_management.admin

# ================= loan improvement =================
import adminpanel.loan_improvement.admin

# ================= concession management =================
import adminpanel.concession_management.admin

# ================= currency management =================
import adminpanel.currency_management.admin

# ================= provisioning classification =================
import adminpanel.provisioning_classification.admin

# ================= collection management =================
import adminpanel.collection_management.admin

# ================= disbursement management =================
import adminpanel.disbursement_management.admin

# ================= document management =================
import adminpanel.document_management.admin

# ================= organization management =================
import adminpanel.organization_management.admin

