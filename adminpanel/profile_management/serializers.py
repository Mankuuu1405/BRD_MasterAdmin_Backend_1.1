from rest_framework import serializers
from .models import *


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"


# =========================
# VENDOR SERIALIZERS
# =========================
class VendorTypeSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = VendorType


class VendorCategorySerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = VendorCategory


class VendorConstitutionSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = VendorConstitution


class VendorLocationSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = VendorLocation


class VendorServiceTypeSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = VendorServiceType


# =========================
# AGENT SERIALIZERS
# =========================
class AgentTypeSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = AgentType


class AgentCategorySerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = AgentCategory


class AgentLevelSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = AgentLevel


class AgentConstitutionSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = AgentConstitution


class AgentLocationSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = AgentLocation


class AgentServiceTypeSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = AgentServiceType


class AgentResponsibilitySerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = AgentResponsibility


# =========================
# CLIENT SERIALIZERS
# =========================
class ClientCategorySerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = ClientCategory


class ClientTypeSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = ClientType


class ClientConstitutionSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = ClientConstitution


class ClientRoleSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = ClientRole


class IndustrySerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Industry


class SectorSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Sector


class ApplicantTypeSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = ApplicantType


class EmploymentTypeSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = EmploymentType


class EmploymentCategorySerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = EmploymentCategory


class EmployerSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Employer


class QualificationSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Qualification


class OccupationTypeSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = OccupationType


class OccupationSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Occupation


class ModeOfOccupationSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = ModeOfOccupation


class InstitutionSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Institution


class MembershipTypeSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = MembershipType


class GenderSalutationSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = GenderSalutation


class RelationshipSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Relationship


class AddressTypeSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = AddressType


class OwnershipSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Ownership


class EmployeeQuotaSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = EmployeeQuota


class GroupLoanSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = GroupLoan
