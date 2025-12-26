from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from .models import *
from .serializers import *

class BaseMasterView(ModelViewSet):
    permission_classes = [IsAdminUser]

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()


# Vendor
class VendorTypeView(BaseMasterView): queryset = VendorType.objects.filter(is_deleted=False); serializer_class = VendorTypeSerializer
class VendorCategoryView(BaseMasterView): queryset = VendorCategory.objects.filter(is_deleted=False); serializer_class = VendorCategorySerializer
class VendorConstitutionView(BaseMasterView): queryset = VendorConstitution.objects.filter(is_deleted=False); serializer_class = VendorConstitutionSerializer
class VendorLocationView(BaseMasterView): queryset = VendorLocation.objects.filter(is_deleted=False); serializer_class = VendorLocationSerializer
class VendorServiceTypeView(BaseMasterView): queryset = VendorServiceType.objects.filter(is_deleted=False); serializer_class = VendorServiceTypeSerializer

# Agent
class AgentTypeView(BaseMasterView): queryset = AgentType.objects.filter(is_deleted=False); serializer_class = AgentTypeSerializer
class AgentCategoryView(BaseMasterView): queryset = AgentCategory.objects.filter(is_deleted=False); serializer_class = AgentCategorySerializer
class AgentLevelView(BaseMasterView): queryset = AgentLevel.objects.filter(is_deleted=False); serializer_class = AgentLevelSerializer
class AgentConstitutionView(BaseMasterView): queryset = AgentConstitution.objects.filter(is_deleted=False); serializer_class = AgentConstitutionSerializer
class AgentLocationView(BaseMasterView): queryset = AgentLocation.objects.filter(is_deleted=False); serializer_class = AgentLocationSerializer
class AgentServiceTypeView(BaseMasterView): queryset = AgentServiceType.objects.filter(is_deleted=False); serializer_class = AgentServiceTypeSerializer
class AgentResponsibilityView(BaseMasterView): queryset = AgentResponsibility.objects.filter(is_deleted=False); serializer_class = AgentResponsibilitySerializer

# Client
class ClientCategoryView(BaseMasterView): queryset = ClientCategory.objects.filter(is_deleted=False); serializer_class = ClientCategorySerializer
class ClientTypeView(BaseMasterView): queryset = ClientType.objects.filter(is_deleted=False); serializer_class = ClientTypeSerializer
class ClientConstitutionView(BaseMasterView): queryset = ClientConstitution.objects.filter(is_deleted=False); serializer_class = ClientConstitutionSerializer
class ClientRoleView(BaseMasterView): queryset = ClientRole.objects.filter(is_deleted=False); serializer_class = ClientRoleSerializer
class IndustryView(BaseMasterView): queryset = Industry.objects.filter(is_deleted=False); serializer_class = IndustrySerializer
class SectorView(BaseMasterView): queryset = Sector.objects.filter(is_deleted=False); serializer_class = SectorSerializer
class ApplicantTypeView(BaseMasterView): queryset = ApplicantType.objects.filter(is_deleted=False); serializer_class = ApplicantTypeSerializer
class EmploymentTypeView(BaseMasterView): queryset = EmploymentType.objects.filter(is_deleted=False); serializer_class = EmploymentTypeSerializer
class EmploymentCategoryView(BaseMasterView): queryset = EmploymentCategory.objects.filter(is_deleted=False); serializer_class = EmploymentCategorySerializer
class EmployerView(BaseMasterView): queryset = Employer.objects.filter(is_deleted=False); serializer_class = EmployerSerializer
class QualificationView(BaseMasterView): queryset = Qualification.objects.filter(is_deleted=False); serializer_class = QualificationSerializer
class OccupationTypeView(BaseMasterView): queryset = OccupationType.objects.filter(is_deleted=False); serializer_class = OccupationTypeSerializer
class OccupationView(BaseMasterView): queryset = Occupation.objects.filter(is_deleted=False); serializer_class = OccupationSerializer
class ModeOfOccupationView(BaseMasterView): queryset = ModeOfOccupation.objects.filter(is_deleted=False); serializer_class = ModeOfOccupationSerializer
class InstitutionView(BaseMasterView): queryset = Institution.objects.filter(is_deleted=False); serializer_class = InstitutionSerializer
class MembershipTypeView(BaseMasterView): queryset = MembershipType.objects.filter(is_deleted=False); serializer_class = MembershipTypeSerializer
class GenderSalutationView(BaseMasterView): queryset = GenderSalutation.objects.filter(is_deleted=False); serializer_class = GenderSalutationSerializer
class RelationshipView(BaseMasterView): queryset = Relationship.objects.filter(is_deleted=False); serializer_class = RelationshipSerializer
class AddressTypeView(BaseMasterView): queryset = AddressType.objects.filter(is_deleted=False); serializer_class = AddressTypeSerializer
class OwnershipView(BaseMasterView): queryset = Ownership.objects.filter(is_deleted=False); serializer_class = OwnershipSerializer
class EmployeeQuotaView(BaseMasterView): queryset = EmployeeQuota.objects.filter(is_deleted=False); serializer_class = EmployeeQuotaSerializer
class GroupLoanView(BaseMasterView): queryset = GroupLoan.objects.filter(is_deleted=False); serializer_class = GroupLoanSerializer
