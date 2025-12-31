from django.contrib import admin
from .models import *

# Auto-register all masters
MASTER_MODELS = [
    VendorType, VendorCategory, VendorConstitution, VendorLocation, VendorServiceType,
    AgentType, AgentCategory, AgentLevel, AgentConstitution, AgentServiceType,
    AgentLocation, AgentResponsibility,
    ClientCategory, ClientType, ClientConstitution, ClientRole,
    Industry, Sector, ApplicantType, EmploymentType, EmploymentCategory,
    EmployerType, Qualification, OccupationType, Occupation, ModeOfOccupation,
    Institution, MembershipType, GenderSalute, Relationship, AddressType, Ownership,
]

for model in MASTER_MODELS:
    admin.site.register(model)


@admin.register(VendorProfile)
class VendorProfileAdmin(admin.ModelAdmin):
    list_display = (
        "vendor_type",
        "vendor_category",
        "vendor_constitution",
        "vendor_location",
        "vendor_service_type",
        "is_active",
    )


@admin.register(AgentProfile)
class AgentProfileAdmin(admin.ModelAdmin):
    list_display = (
        "agent_type",
        "agent_category",
        "agent_level",
        "agent_location",
        "is_active",
    )


@admin.register(ClientProfile)
class ClientProfileAdmin(admin.ModelAdmin):
    list_display = (
        "client_category",
        "client_type",
        "employment_type",
        "industry",
        "is_active",
    )
