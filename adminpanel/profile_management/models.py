from django.db import models

# =========================
# COMMON BASE
# =========================
class BaseMaster(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


# =========================
# VENDOR MASTERS
# =========================
class VendorType(BaseMaster):
    pass


class VendorCategory(BaseMaster):
    pass


class VendorConstitution(BaseMaster):
    pass


class VendorLocation(BaseMaster):
    pass


class VendorServiceType(BaseMaster):
    pass


class VendorProfile(models.Model):
    vendor_type = models.ForeignKey(VendorType, on_delete=models.PROTECT)
    vendor_category = models.ForeignKey(VendorCategory, on_delete=models.PROTECT)
    vendor_constitution = models.ForeignKey(VendorConstitution, on_delete=models.PROTECT)
    vendor_location = models.ForeignKey(VendorLocation, on_delete=models.PROTECT)
    vendor_service_type = models.ForeignKey(VendorServiceType, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.vendor_type} - {self.vendor_category}"


# =========================
# AGENT MASTERS
# =========================
class AgentType(BaseMaster):
    pass


class AgentCategory(BaseMaster):
    pass


class AgentLevel(BaseMaster):
    pass


class AgentConstitution(BaseMaster):
    pass


class AgentServiceType(BaseMaster):
    pass


class AgentLocation(BaseMaster):
    pass


class AgentResponsibility(BaseMaster):
    pass


class AgentProfile(models.Model):
    agent_type = models.ForeignKey(AgentType, on_delete=models.PROTECT)
    agent_category = models.ForeignKey(AgentCategory, on_delete=models.PROTECT)
    agent_level = models.ForeignKey(AgentLevel, on_delete=models.PROTECT)
    agent_constitution = models.ForeignKey(AgentConstitution, on_delete=models.PROTECT)
    agent_service_type = models.ForeignKey(AgentServiceType, on_delete=models.PROTECT)
    agent_location = models.ForeignKey(AgentLocation, on_delete=models.PROTECT)
    agent_responsibility = models.ManyToManyField(AgentResponsibility)
    is_active = models.BooleanField(default=True)


# =========================
# CLIENT MASTERS (FOR DROPDOWNS)
# =========================
class ClientCategory(BaseMaster):
    pass


class ClientType(BaseMaster):
    pass


class ClientConstitution(BaseMaster):
    pass


class ClientRole(BaseMaster):
    pass


class Industry(BaseMaster):
    pass


class Sector(BaseMaster):
    pass


class ApplicantType(BaseMaster):
    pass


class EmploymentType(BaseMaster):
    pass


class EmploymentCategory(BaseMaster):
    pass


class EmployerType(BaseMaster):
    pass


class Qualification(BaseMaster):
    pass


class OccupationType(BaseMaster):
    pass


class Occupation(BaseMaster):
    pass


class ModeOfOccupation(BaseMaster):
    pass


class Institution(BaseMaster):
    pass


class MembershipType(BaseMaster):
    pass


class GenderSalute(BaseMaster):
    pass


class Relationship(BaseMaster):
    pass


class AddressType(BaseMaster):
    pass


class Ownership(BaseMaster):
    pass


class ClientProfile(models.Model):
    client_category = models.ForeignKey(ClientCategory, on_delete=models.PROTECT)
    client_type = models.ForeignKey(ClientType, on_delete=models.PROTECT)
    constitution = models.ForeignKey(ClientConstitution, on_delete=models.PROTECT)
    role = models.ForeignKey(ClientRole, on_delete=models.PROTECT)
    industry = models.ForeignKey(Industry, on_delete=models.PROTECT)
    sector = models.ForeignKey(Sector, on_delete=models.PROTECT)
    applicant_type = models.ForeignKey(ApplicantType, on_delete=models.PROTECT)
    employment_type = models.ForeignKey(EmploymentType, on_delete=models.PROTECT)
    employment_category = models.ForeignKey(EmploymentCategory, on_delete=models.PROTECT)
    employer_type = models.ForeignKey(EmployerType, on_delete=models.PROTECT)
    employer = models.CharField(max_length=150)
    qualification = models.ForeignKey(Qualification, on_delete=models.PROTECT)
    occupation_type = models.ForeignKey(OccupationType, on_delete=models.PROTECT)
    occupation = models.ForeignKey(Occupation, on_delete=models.PROTECT)
    mode_of_occupation = models.ForeignKey(ModeOfOccupation, on_delete=models.PROTECT)
    institution = models.ForeignKey(Institution, on_delete=models.PROTECT)
    membership_type = models.ForeignKey(MembershipType, on_delete=models.PROTECT)
    gender_salute = models.ForeignKey(GenderSalute, on_delete=models.PROTECT)
    relationship = models.ForeignKey(Relationship, on_delete=models.PROTECT)
    address_type = models.ForeignKey(AddressType, on_delete=models.PROTECT)
    ownership = models.ForeignKey(Ownership, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
