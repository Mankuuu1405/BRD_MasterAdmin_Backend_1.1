from django.db import models
import uuid

STATUS_CHOICES = (
    ("ACTIVE", "Active"),
    ("INACTIVE", "Inactive"),
)

# =================================================
# COMMON BASE
# =================================================
class BaseProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="ACTIVE")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


# =================================================
# VENDOR PROFILE MANAGEMENT
# (Type, Category, Constitution, Location, Service Type)
# =================================================
class VendorType(BaseProfile):
    pass

class VendorCategory(BaseProfile):
    pass

class VendorConstitution(BaseProfile):
    pass

class VendorLocation(BaseProfile):
    pass

class VendorServiceType(BaseProfile):
    pass


# =================================================
# AGENT PROFILE MANAGEMENT
# =================================================
class AgentType(BaseProfile):
    pass

class AgentCategory(BaseProfile):
    pass

class AgentLevel(BaseProfile):
    pass

class AgentConstitution(BaseProfile):
    pass

class AgentLocation(BaseProfile):
    pass

class AgentServiceType(BaseProfile):
    pass

class AgentResponsibility(BaseProfile):
    pass


# =================================================
# CLIENT PROFILE MANAGEMENT
# =================================================
class ClientCategory(BaseProfile):
    pass

class ClientType(BaseProfile):
    pass

class ClientConstitution(BaseProfile):
    pass

class ClientRole(BaseProfile):
    pass

class Industry(BaseProfile):
    pass

class Sector(BaseProfile):
    pass

class ApplicantType(BaseProfile):
    pass

class EmploymentType(BaseProfile):
    pass

class EmploymentCategory(BaseProfile):
    pass

class Employer(BaseProfile):
    pass

class Qualification(BaseProfile):
    pass

class OccupationType(BaseProfile):
    pass

class Occupation(BaseProfile):
    pass

class ModeOfOccupation(BaseProfile):
    pass

class Institution(BaseProfile):
    pass

class MembershipType(BaseProfile):
    pass

class GenderSalutation(BaseProfile):
    pass

class Relationship(BaseProfile):
    pass

class AddressType(BaseProfile):
    pass

class Ownership(BaseProfile):
    pass

class EmployeeQuota(BaseProfile):
    pass

class GroupLoan(BaseProfile):
    pass
