from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register("vendor-types", VendorTypeView)
router.register("vendor-categories", VendorCategoryView)
router.register("vendor-constitutions", VendorConstitutionView)
router.register("vendor-locations", VendorLocationView)
router.register("vendor-service-types", VendorServiceTypeView)

router.register("agent-types", AgentTypeView)
router.register("agent-categories", AgentCategoryView)
router.register("agent-levels", AgentLevelView)
router.register("agent-constitutions", AgentConstitutionView)
router.register("agent-locations", AgentLocationView)
router.register("agent-service-types", AgentServiceTypeView)
router.register("agent-responsibilities", AgentResponsibilityView)

router.register("client-categories", ClientCategoryView)
router.register("client-types", ClientTypeView)
router.register("client-constitutions", ClientConstitutionView)
router.register("client-roles", ClientRoleView)
router.register("industries", IndustryView)
router.register("sectors", SectorView)
router.register("applicant-types", ApplicantTypeView)
router.register("employment-types", EmploymentTypeView)
router.register("employment-categories", EmploymentCategoryView)
router.register("employers", EmployerView)
router.register("qualifications", QualificationView)
router.register("occupation-types", OccupationTypeView)
router.register("occupations", OccupationView)
router.register("modes-of-occupation", ModeOfOccupationView)
router.register("institutions", InstitutionView)
router.register("membership-types", MembershipTypeView)
router.register("gender-salutations", GenderSalutationView)
router.register("relationships", RelationshipView)
router.register("address-types", AddressTypeView)
router.register("ownerships", OwnershipView)
router.register("employee-quotas", EmployeeQuotaView)
router.register("group-loans", GroupLoanView)

urlpatterns = router.urls
