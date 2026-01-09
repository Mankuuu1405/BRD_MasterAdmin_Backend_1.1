# from django.db.models.signals import post_migrate
# from django.dispatch import receiver
# from django.contrib.auth import get_user_model

# from .models import Role, Permission, RolePermission, UserRole


# @receiver(post_migrate)
# def setup_master_admin(sender, **kwargs):
#     """
#     Runs after migrate:
#     - creates all permissions
#     - creates Master Admin role
#     - assigns all permissions to Master Admin
#     """

#     # 🔑 ALL PERMISSIONS (single source of truth)
#     permission_list = [
#         ("dashboard.view", "View dashboard"),
#         ("organizations.view", "View organizations"),
#         ("users.view", "View users"),
#         ("roles.view", "View roles"),
#         ("subscriptions.view", "View subscriptions"),

#         ("approval.view", "View approvals"),
#         ("approval.manage", "Manage approvals"),
#         ("approval.escalation", "Approval escalation"),

#         ("product.view", "View products"),
#         ("product.manage", "Manage products"),
#         ("product.mix", "Manage product mix"),
#         ("fees.view", "View fees"),
#         ("charges.view", "View charges"),
#         ("interest.view", "View interest"),
#         ("repayment.view", "View repayment"),
#         ("penalties.view", "View penalties"),
#         ("moratorium.view", "View moratorium"),

#         ("loan.view", "View loan improvement"),
#         ("currency.view", "View currency"),
#         ("concession.view", "View concession"),

#         ("eligibility.view", "View eligibility"),
#         ("eligibility.create", "Create eligibility"),
#         ("eligibility.update", "Update eligibility"),

#         ("banking.view", "View banking"),
#         ("banking.create", "Create banking"),
#         ("banking.update", "Update banking"),

#         ("obligation.view", "View obligation"),
#         ("obligation.create", "Create obligation"),
#         ("obligation.update", "Update obligation"),

#         ("score.view", "View score card"),
#         ("score.create", "Create score card"),
#         ("score.update", "Update score card"),

#         ("template.view", "View templates"),
#         ("template.predefine", "Predefine templates"),
#         ("template.customize", "Customize templates"),

#         ("bankfund.view", "View bank & fund"),
#         ("bank.view", "View bank"),
#         ("fund.view", "View fund"),
#         ("portfolio.view", "View portfolio"),
#         ("mode.view", "View mode of bank"),
#         ("tax.view", "View taxation"),
#         ("business.view", "View business model"),

#         ("profile.view", "View profiles"),
#         ("profile.vendor", "Vendor profile"),
#         ("profile.agent", "Agent profile"),
#         ("profile.client", "Client profile"),

#         ("agent.view", "View agents"),
#         ("agent.channel", "Channel partner"),
#         ("agent.verification", "Verification agency"),
#         ("agent.collection", "Collection agent"),
#         ("agent.legal", "Legal agent"),

#         ("controls.view", "View controls"),
#         ("controls.language", "Manage language"),
#         ("controls.geo", "Manage geo"),
#         ("controls.login", "Login authentication"),
#         ("controls.coapplicant", "Co-applicant"),
#         ("controls.loginfee", "Login fee"),
#         ("controls.joint", "Joint applicant"),
#         ("controls.references", "References"),
#         ("controls.application", "Application process"),
#         ("controls.scorecard", "Score card rating"),
#         ("controls.verification", "Verification"),

#         ("rules.view", "View rules"),
#         ("rules.master", "Rule master"),
#         ("rules.impact", "Impact values"),
#         ("rules.client", "Client profile rules"),
#         ("rules.collateral", "Collateral quality"),
#         ("rules.financial", "Financial eligibility"),
#         ("rules.scorecard", "Rule score card"),
#         ("rules.risk", "Risk & mitigation"),
#         ("rules.verification", "Verification rules"),

#         ("audit.view", "View audits"),
#         ("reports.view", "View reports"),

#         ("employment.view", "View employment types"),
#         ("occupation.view", "View occupation types"),
#     ]

#     # 1️⃣ Create permissions
#     permission_objs = []
#     for code, desc in permission_list:
#         perm, _ = Permission.objects.get_or_create(
#             code=code,
#             defaults={"description": desc}
#         )
#         permission_objs.append(perm)

#     # 2️⃣ Create Master Admin role
#     master_role, _ = Role.objects.get_or_create(
#         name="Master Admin",
#         defaults={
#             "description": "System super administrator",
#             "is_active": True,
#         }
#     )

#     # 3️⃣ Assign all permissions to Master Admin
#     for perm in permission_objs:
#         RolePermission.objects.get_or_create(
#             role=master_role,
#             permission=perm
#         )


# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib.auth import get_user_model


# User = get_user_model()


# @receiver(post_save, sender=User)
# def assign_master_admin_to_superuser(sender, instance, created, **kwargs):
#     """
#     Whenever createsuperuser is run:
#     - Assign Master Admin role automatically
#     """

#     if not instance.is_superuser:
#         return

#     master_role = Role.objects.filter(name="Master Admin").first()
#     if not master_role:
#         return

#     UserRole.objects.get_or_create(
#         user=instance,
#         role=master_role
#     )


from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.apps import apps

User = get_user_model()

# ------------------- POST MIGRATE -------------------
@receiver(post_migrate)
def setup_master_admin(sender, **kwargs):
    Role = apps.get_model("access_control", "Role")
    Permission = apps.get_model("access_control", "Permission")
    RolePermission = apps.get_model("access_control", "RolePermission")
    UserRole = apps.get_model("access_control", "UserRole")

    # Create Master Admin role
    master_role, _ = Role.objects.get_or_create(
        name="Master Admin",
        defaults={"description": "System Super Administrator"}
    )

    # Define all permissions
    PERMISSIONS = [
        ("dashboard.view", "View dashboard"),
        ("organizations.view", "View organizations"),
        ("users.view", "View users"),
        ("roles.view", "View roles"),
        ("subscriptions.view", "View subscriptions"),

        ("approval.view", "View approvals"),
        ("approval.manage", "Manage approvals"),
        ("approval.escalation", "Approval escalation"),

        ("product.view", "View products"),
        ("product.manage", "Manage products"),
        ("product.mix", "Manage product mix"),
        ("fees.view", "View fees"),
        ("charges.view", "View charges"),
        ("interest.view", "View interest"),
        ("repayment.view", "View repayment"),
        ("penalties.view", "View penalties"),
        ("moratorium.view", "View moratorium"),

        ("loan.view", "View loan improvement"),
        ("currency.view", "View currency"),
        ("concession.view", "View concession"),

        ("eligibility.view", "View eligibility"),
        ("eligibility.create", "Create eligibility"),
        ("eligibility.update", "Update eligibility"),

        ("banking.view", "View banking"),
        ("banking.create", "Create banking"),
        ("banking.update", "Update banking"),

        ("obligation.view", "View obligation"),
        ("obligation.create", "Create obligation"),
        ("obligation.update", "Update obligation"),

        ("score.view", "View score card"),
        ("score.create", "Create score card"),
        ("score.update", "Update score card"),

        ("template.view", "View templates"),
        ("template.predefine", "Predefine templates"),
        ("template.customize", "Customize templates"),

        ("bankfund.view", "View bank & fund"),
        ("bank.view", "View bank"),
        ("fund.view", "View fund"),
        ("portfolio.view", "View portfolio"),
        ("mode.view", "View mode of bank"),
        ("tax.view", "View taxation"),
        ("business.view", "View business model"),

        ("profile.view", "View profiles"),
        ("profile.vendor", "Vendor profile"),
        ("profile.agent", "Agent profile"),
        ("profile.client", "Client profile"),

        ("agent.view", "View agents"),
        ("agent.channel", "Channel partner"),
        ("agent.verification", "Verification agency"),
        ("agent.collection", "Collection agent"),
        ("agent.legal", "Legal agent"),

        ("controls.view", "View controls"),
        ("controls.language", "Manage language"),
        ("controls.geo", "Manage geo"),
        ("controls.login", "Login authentication"),
        ("controls.coapplicant", "Co-applicant"),
        ("controls.loginfee", "Login fee"),
        ("controls.joint", "Joint applicant"),
        ("controls.references", "References"),
        ("controls.application", "Application process"),
        ("controls.scorecard", "Score card rating"),
        ("controls.verification", "Verification"),

        ("rules.view", "View rules"),
        ("rules.master", "Rule master"),
        ("rules.impact", "Impact values"),
        ("rules.client", "Client profile rules"),
        ("rules.collateral", "Collateral quality"),
        ("rules.financial", "Financial eligibility"),
        ("rules.scorecard", "Rule score card"),
        ("rules.risk", "Risk & mitigation"),
        ("rules.verification", "Verification rules"),

        ("audit.view", "View audits"),
        ("reports.view", "View reports"),

        ("employment.view", "View employment types"),
        ("occupation.view", "View occupation types"),
    ]

    # Create permissions + attach to Master Admin
    for code, desc in PERMISSIONS:
        perm, _ = Permission.objects.get_or_create(code=code, defaults={"description": desc})
        RolePermission.objects.get_or_create(role=master_role, permission=perm)

    # Assign role to all superusers
    for user in User.objects.filter(is_superuser=True):
        UserRole.objects.get_or_create(user=user, role=master_role)

# ------------------- POST SAVE -------------------
@receiver(post_save, sender=User)
def assign_master_admin_role(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        Role = apps.get_model("access_control", "Role")
        UserRole = apps.get_model("access_control", "UserRole")

        master_role, _ = Role.objects.get_or_create(
            name="Master Admin",
            defaults={"description": "System Super Administrator"}
        )

        UserRole.objects.get_or_create(user=instance, role=master_role)
