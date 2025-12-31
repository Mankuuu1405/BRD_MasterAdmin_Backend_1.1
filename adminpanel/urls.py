from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    LoginView,
    RoleViewSet,
    LoanProductViewSet,
    ProductFacilityViewSet,
    InterestConfigViewSet,
    FeeConfigViewSet,
    ChargeConfigViewSet,
    PenaltyConfigViewSet,
    RepaymentConfigViewSet,
    MoratoriumConfigViewSet,
    ProductMixViewSet,
)

router = DefaultRouter()
router.register("roles", RoleViewSet)
router.register("loan-products", LoanProductViewSet)
router.register("product-facilities", ProductFacilityViewSet)
router.register("interest-configs", InterestConfigViewSet)
router.register("fee-configs", FeeConfigViewSet)
router.register("charge-configs", ChargeConfigViewSet)
router.register("penalty-configs", PenaltyConfigViewSet)
router.register("repayment-configs", RepaymentConfigViewSet)
router.register("moratorium-configs", MoratoriumConfigViewSet)
router.register("product-mixes", ProductMixViewSet)

urlpatterns = [
    path("login/", LoginView.as_view(), name="admin-login"),
    path("product-management/", include("adminpanel.product_management.urls")),
    path("access-control/", include("adminpanel.access_control.urls")),
    path("approval-master/", include("adminpanel.approval_master.urls")),
    path("home-dashboard/", include("adminpanel.home_dashboard.urls")),
    path("subscription/", include("adminpanel.subscription_management.urls")),
    path("coupon/", include("adminpanel.coupon_management.urls")),
   
    path("rule-management/", include("adminpanel.rule_management.urls")),
    path("agent/", include("adminpanel.agent_management.urls")),
    path("currency-management/", include("adminpanel.currency_management.urls")),
    path("concession-management/", include("adminpanel.concession_management.urls")),
    path("profile-management/", include("adminpanel.profile_management.urls")),
    path("controls-management/", include("adminpanel.system_settings.urls")),
    path("", include(router.urls)),
]
