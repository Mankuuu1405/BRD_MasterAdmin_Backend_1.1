from django.apps import AppConfig

class AdminpanelConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "adminpanel"

    def ready(self):
        from adminpanel.access_control import models
        from adminpanel.product_management import models
        from adminpanel.product_mix_management import models
        from adminpanel.approval_master import models
        from adminpanel.eligibility_score_management import models
        from adminpanel.risk_mitigation_management import models
        from adminpanel.subscription_management import models
        from adminpanel.bank_funds_management import models
        from adminpanel.agent_management import models
        from adminpanel.profile_management import models
        from adminpanel.audit_logs import models
